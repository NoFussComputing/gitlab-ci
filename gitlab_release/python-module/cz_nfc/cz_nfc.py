#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import git as Git
import re

from commitizen import git
from commitizen.cz.base import BaseCommitizen


class nfc_cz(BaseCommitizen):
    bump_pattern = r"^(break|new|fix|feat|hotfix|ci|docs)"
    bump_map = {"break": "MAJOR", "new": "MINOR", "feat": "MINOR","fix": "PATCH", "hotfix": "PATCH", "ci": "PATCH", "docs": "PATCH"}

    changelog_pattern = "^(break|new|fix|feat|hotfix|refactor|ci|docs)"
    change_type_order = ["BREAKING CHANGE", "feat", "fix", "refactor", "perf", "docs", "ci"]
    change_type_map = {
        "feat": "Features",
        "fix": "Bug Fixes",
        "refactor": "Code Refactor",
        "perf": "Performance improvements",
        "docs": "Documentaton / Guides",
        "ci": "Continious Integration"
    }

    commit_parser = r"^(?P<change_type>feat|fix|refactor|perf|BREAKING CHANGE|refactor|ci|docs)(?:\((?P<scope>[^()\r\n]*)\)|\()?(?P<breaking>!)?:\s(?P<message>.*)?"


    def changelog_message_builder_hook(self, parsed_message: dict, commit: git.GitCommit) -> dict:
        rev = commit.rev
        rev_short = str(rev)[0:8]
        repo = Git.Repo(os.getcwd())

        tree = list(repo.iter_commits(repo.active_branch))

        footer_references = ''
        for item in tree:

            if item.message.count("\n") > 2 and str(item).lower() == rev.lower():
                footer_line = item.message.split("\n")
                footer_line = footer_line[(len(footer_line)-1)]
                footer = re.findall(r"([\!|\#][0-9]+)", str(item.message))

                try:

                    for reference in footer:

                        if '#' in reference:

                            footer_references += ' ' + str(
                                '[{0}]({1}/-/issues/{2})'.format(
                                    reference,
                                    os.environ['CI_PROJECT_URL'],
                                    reference.replace('#', '')
                                 )
                             )

                        if '!' in reference:
                            footer_references += ' ' + str(
                                '[{0}]({1}/-/merge_requests/{2})'.format(
                                    reference,
                                    os.environ['CI_PROJECT_URL'],
                                    reference.replace('!', '')
                                )
                            )

                except Exception:
                    pass

        if footer_references != '':
            footer_references = ' [' + footer_references + ' ]'

        m = parsed_message["message"]
        parsed_message["message"] = f"[{rev_short}](" + os.environ['CI_PROJECT_URL'] + f"/-/commit/{rev}) - {m}" + footer_references

        return parsed_message


    def questions(self) -> list:
        raise NotImplementedError("Not Implemented yet")

    def message(self, answers: dict) -> str:
        raise NotImplementedError("Not Implemented yet")


discover_this = nfc_cz
