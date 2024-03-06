## 0.7.0rc0 (2024-02-02)

### Bug Fixes

- **mkdocs**: [3fa71fe9](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3fa71fe91ad1e874b76fab7323e02496ac757f5d) - correct mkdocs image name [ [!73](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/73) ]
- **commit_footer_refs**: [0f6e06c5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0f6e06c50f7cae602cdc2ca00bbce7fe1fd72c32) - enable automated jobs without MR to succeed. [ [#44](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/44) [!72](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/72) ]
- **commit_footer_refs**: [b8199586](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b8199586b4fe4c9f93efe68a908eaa8582f064c3) - dont update git submodules [ [!71](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/71) [#42](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/42) [!2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/2) ]

### Code Refactor

- **mkdocs**: [955ce375](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/955ce3752050e78085c2037fe66714db41114c9e) - set env name to gitlab pages [ [!73](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/73) [#43](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/43) ]

### Features

- **sub_module_update**: [fc9f3761](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/fc9f37617cd26b3e44326161ba10183eb13444dd) - wbsite-template [ [!44](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/44) ]
- **mkdocs**: [3fbd4317](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3fbd4317c0388fb8e406eb78614e3943375496ed) - update requirements.txt to current versions [ [!73](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/73) [!13](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/13) [!44](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/44) ]
- **mkdocs**: [c4087c70](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/c4087c7069524df573a43db29c399940600ddba7) - update python to 3.11.2 [ [!73](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/73) [!13](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/13) [!44](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/44) ]

## 0.6.1 (2023-11-06)

### Bug Fixes

- **docker**: [359c664d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/359c664d97c516bd3b35fb46961288c74f6bd940) - always build on tag [ [!68](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/68) [#37](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/37) ]
- **build**: [799de6c9](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/799de6c98c0925ef4a85cf246512041fc89534db) - adjust to enforce [ [!66](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/66) ]
- **docker**: [4ea999ce](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4ea999cec96824c2670c5d448dff8c06b1582adc) - ensure on any changes to directory path, build occurs [ [!64](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/64) [#38](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/38) [!76](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/76) ]
- **template**: [4da44b77](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4da44b77dfbc015d28fda34fcfe54d70a6542943) - issue comment patch remove setting role path [ [!62](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/62) ]

### Code Refactor

- **ansible**: [d21692f7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d21692f7886986db1808befb00b045c1a9a65a8f) - move submodule/issue patch to mr pipeline [ [!67](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/67) ]

### Continious Integration

- **deploy**: [f35d99dc](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f35d99dc436d1e9ab200a8b94052de2fa23608fc) - added docker management repo [ [!63](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/63) ]

### Documentaton / Guides

- [535d0b42](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/535d0b42938fc66f94fd57018dd81e2111ad3abe) - update docker tag build [ [!68](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/68) [#37](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/37) ]
- [d9b303ed](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d9b303edc1f61f1d7a4785b5b5396625cc98a179) - expand [ [!59](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/59) ]

### Features

- **conventional_commits**: [3918686e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3918686e483f6fabb6c487be6f2d7105da08d11a) - do not run on master branch [ [!70](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/70) [#40](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/40) ]
- **sub_module_update**: [8eb57c58](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8eb57c580973fa49bd3ffb12553cc24e39c5afac) - enable passing commit type and category [ [!69](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/69) [#39](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/39) [!122](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/122) [#39](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/39) [!96](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/96) [!28](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/28) ]
- **deploy**: [86a0292f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/86a0292fafa0fb139f068106dacfa2ee6917f4d4) - add new nfc repos [ [!68](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/68) ]
- **release**: [837311c0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/837311c0221820b93072e9bfcba2191a8b96b9ea) - annotate git tag with changelog [ [!68](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/68) ]
- **build**: [e8758c4c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e8758c4ccecdbf0c22a5e67bf086762c68c6b915) - no docs/docker build on master push, only tag [ [!68](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/68) ]
- **docker**: [0d797415](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0d7974152c26200c8beaa3a1ddecf504f4406ee3) - add debugging to publish [ [#36](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/36) [!68](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/68) [#36](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/36) [#11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/11) ]
- **deploy**: [1a168593](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1a168593eb0fd234885982a16bc216804e76d293) - added ansible.docker.os repo [ [!67](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/67) ]
- **docker_publish**: [9489c99f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9489c99fe489c9b9b9e29fc2013d5ff6a990094a) - on merge to dev always publish [ [!65](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/65) ]
- **template**: [da40e027](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/da40e027376c163ca4915f3edcf322b6e0b0c278) - added auto job mr from issue comment patch [ [!61](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/61) ]

## 0.6.1rc8 (2023-06-08)

### Bug Fixes

- **lint**: [4462ec04](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4462ec04268c5b967f0672828d1cd7b3995894d9) - all lint to immediatly start job [ [!57](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/57) ]
- **ci**: [9b00af99](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9b00af996ff96f58a26b83066004e5a9e94ac155) - correct dockerhub tag [ [!57](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/57) ]
- **ci**: [6af454be](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6af454be4d2b658e0c362392ff502b3fb3da2cbf) - remove spaces from regex exists and changes [ [!56](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/56) ]
- **ansible_lint**: [46d85bcf](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/46d85bcf49ea73545a5af4324c28af51a17acd3c) - enable first level dir paths [ [!55](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/55) ]
- **docker_build**: [11b62099](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/11b6209992294e45a051e26963d772d75014e516) - on success push container to docker hub [ [!53](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/53) ]
- **docker_build**: [e90b938b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e90b938bba092bdaecbc1a43758218da0058427b) - init submodule submodules [ [!53](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/53) ]

### Documentaton / Guides

- [469255f4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/469255f450e946a712d379415e45a74eb8c07995) - added notes [ [!58](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/58) ]

### Features

- **ci**: [0ec520f0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0ec520f02328b69642f929a19e8517c7d475a988) - add resource groups [ [!55](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/55) [#33](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/33) ]
- **sync**: [e75464c7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e75464c7c409fd17864624d48c9fec8e6e3544e9) - immediatee git sync [ [!55](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/55) ]
- **latest_artifacts**: [755fcac0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/755fcac06e9f265789b02a88eb90df35ab1dbf07) - ensure artifats for jobs are always avail on branches [ [!54](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/54) [#34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/34) [#331232](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/331232) ]
- **latest_artifacts**: [22dd4985](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/22dd4985be315be95be55b2b4edff5ae4ba1eeb4) - ensure artifats for jobs are always avail on branches [ [!52](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/52) [#34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/34) [#331232](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/331232) ]

## 0.6.1rc7 (2023-06-05)

### Bug Fixes

- **mkdocs**: [5ffc68d7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5ffc68d7241bb0c729a990b4a5b060bd6488ea8c) - adjust rules to match lint [ [!51](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/51) ]
- **docker**: [097725c1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/097725c1be5d155cebada0cf2cbb17ddbd041e6e) - detect canges in include path corrected [ [!50](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/50) ]
- **ci**: [9e098245](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9e098245d7a6272fd51aee0a479af3a233fdb30e) - typo in docker build [ [!49](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/49) [!20](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/20) ]
- **ansible_playbook**: [13ee3bf5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/13ee3bf535dadf7cada645ddec74e2e29872ac2c) - No4 enable parent pipelines [ [!47](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/47) ]
- **ansible_playbook**: [3c0543f7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3c0543f7ad0673bcb6600e6ff20693be5f784f23) - No3 enable parent pipelines [ [!45](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/45) ]
- **ansible_playbook**: [f3fa9c5a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f3fa9c5a416295cb2a0362a31f05995336ea9155) - enable parent pipelines [ [!45](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/45) ]
- **ansible_playbook**: [3ee48daa](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3ee48daa10eee6dd80b79ed076c4ad4d1ff9bb57) - enable parent pipelines [ [!44](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/44) ]

### Features

- **ansible_lint**: [6a149f6e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6a149f6ed6d514c42d67b6b04cea114aa32067b8) - added inventory & playbooks directories [ [!50](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/50) [#22](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/22) [!27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/27) ]
- **ci**: [1dcb3ed5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1dcb3ed521538de47745ed00148bb4123708d90d) - dont git submodule recurse [ [!50](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/50) ]
- **commit_footer_refs**: [f3256c58](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f3256c5858e1b5b2b6444f9d8ae63f556f4acb30) - only run on changes [ [!50](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/50) ]
- **ci**: [d8a6d5f7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d8a6d5f7ec1f73d5ae506301666383aac843708d) - git gubmodule update trigger moved to api call via curl [ [!48](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/48) [!62](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/62) ]
- **ci**: [35cfa92c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/35cfa92cd900e7ed7008695bf0b65aaf147bb0ec) - git submodule job moved to own definition [ [!48](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/48) [!62](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/62) ]
- **ansible_playbook**: [a86d17ef](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a86d17eff267750c3713968852d5013ef00ee226) - rules set to never 'ONLY' [ [!48](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/48) [!62](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/62) ]

## 0.6.1rc6 (2023-06-02)

### Bug Fixes

- **md_lint**: [ba43bb9c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ba43bb9c8de87d723abcd0b4b7519c88d8c3b162) - lint on git tag [ [!43](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/43) ]

## 0.6.1rc5 (2023-06-02)

### Bug Fixes

- **gitlab_yaml_lint**: [efa62710](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/efa62710571e48872d700a8a8802a526fb86b1f6) - adjust logic to detect changes [ [!42](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/42) ]
- **commit_footer_check**: [6accd863](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6accd8633ca0579de084d9762f610711ae1e5715) - run on non master/dev branches only [ [!42](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/42) ]

### Code Refactor

- **ci**: [9d767282](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9d767282ffa86c48077bd08b605cf50be76a9b07) - update ansible-role repo path [ [!40](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/40) [#74](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/74) ]

### Features

- **submodule_update_trigger**: [86b05338](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/86b05338854f94997cb5cf09fad0561c09f86461) - only update own submodule [ [!41](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/41) [#16](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/16) [!60](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/60) ]
- **mkdocs_build**: [ff8c43c1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ff8c43c1ea2126cabf0ad2f400a784a9f90ec1ac) - always build on git tag [ [!41](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/41) ]
- **ci_rules**: [04e7e928](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/04e7e928e0f4f2212078fd08fd87b2e024dd5257) - add exists and changes for rules [ [!41](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/41) [#32](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/32) ]
- **yaml_anchors**: [862176f9](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/862176f9dca8cf8ee998456db0cc12f7084f7fc0) - initial conditional checks [ [!41](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/41) [#32](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/32) ]
- **ci**: [6f810f80](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6f810f8084e54f0afc9ebb47bfcc855536046a08) - add more repos to update [ [!39](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/39) ]

## 0.6.1rc4 (2023-05-31)

### Bug Fixes

- **ansible_playbook**: [73ea66e6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/73ea66e60d9cdb235aebda839e0a734212c997bc) - always pull image [ [!37](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/37) ]
- **mkdocs_build**: [c47be421](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/c47be42184c96855f0702c0258931da9730df517) - ensure config file exists when run on branch [ [!36](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/36) ]
- **automagic**: [8ced1720](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8ced1720e00f984e75c51bf8985e45d07aac8c09) - fix git submodule so it runs on schedule [ [!35](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/35) [#31](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/31) ]
- **docs_environment**: [b68f6cb4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b68f6cb4b4a571dee52cb765ddb6a5a70c78b364) - don't define empty env path [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **doc_pages**: [91ac4476](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/91ac4476fbefd2476d1c147c1681a1a53cc40201) - use updated job name [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) [#30](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/30) ]
- **ansible_lint**: [75968b14](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/75968b140ca0b2734d6af14e78e7c598b6221600) - only run if tasks/main.yaml exists [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **mkdocs_build_website**: [0bc72554](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0bc72554534488d147356d148d635d490b8a1007) - renamed and normalized [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) [#30](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/30) ]
- **sub_folder_changelog**: [203a9990](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/203a99903c28201f74304ca8689fae25a7a28aa0) - dont create changelog for docs [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **jobs**: [a010f7ba](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a010f7bab19fc89f71c8bc5a81a3d1944f4bdc05) - jobs that occur on push should also run on 'trigger' [ [!33](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/33) [#26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/26) ]
- **docker_publish**: [79855cdb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/79855cdb99762fd444bedddb6be59cb4ba41fe50) - job only run on dockerfile exists [ [!32](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/32) [#28](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/28) ]
- **docker**: [502f12c2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/502f12c21689f86675a000e51ca415019fcad184) - job only run on dockerfile exists [ [!31](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/31) [#28](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/28) ]

### Code Refactor

- [e79b5545](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e79b554550dbabe5df429d6c57fe15cb2b144432) - rename website to documentation [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **ci**: [681b8f1a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/681b8f1a0293986a0b67ba13c72bf8dd92ca692a) - update deploy job name [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **docker_hub**: [7b4b01bd](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7b4b01bdab2c4299e892071ef3c19b324bf3768c) - move needs to template [ [!31](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/31) ]

### Documentaton / Guides

- [87165450](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/871654508cd183afc1240c9c5de16e9f762c89ee) - refine [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **automagic**: [95bc6a5b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/95bc6a5b036d809ef4bce8af6f70568c595785eb) - added initial autmagic docs [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **ansible_playbook**: [39881505](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/398815055e013059afc6c4d99fa97bdeeb003909) - document ci job definition [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) [#26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/26) [#27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/27) ]

### Features

- **ci**: [7018440d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7018440dcbd09c2eb406817eab7df3e24e19687d) - on push to dev, update git sub modules on specified [ [!38](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/38) ]
- **mkdocs_build_docs**: [5e491285](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5e4912857aea43678b2ef61230df3817f193d684) - keyword needs does not belong in definition [ [!36](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/36) ]
- **lint_markdown_docs**: [9ebd0a27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9ebd0a27f65b36b289b3e7c0647e839b5f7a2798) - ensure also detects website [ [!36](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/36) ]
- **ci**: [44076553](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/440765537dcc4370d6558ec5d41fe7f87a5f7f4d) - use automagic ci template [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **automagic**: [18bc18c2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/18bc18c29b4ae08963d4c744e9479622b2cd921c) - add ansible template [ [!34](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/34) ]
- **ansible_play**: [fff7d314](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/fff7d31498d486b1c39f1672df9b283ad02c21d8) - force output colour in job logs [ [!33](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/33) ]

## 0.6.1rc3 (2023-05-28)

### Bug Fixes

- **scheduled_pipelines**: [bade89c5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/bade89c5333ca853844e224f46a2d3dafab7179d) - if scheduled pipeline only run schedualable jobs [ [!30](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/30) [#29](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/29) ]

### Code Refactor

- **ansible_playbook**: [f9af921e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f9af921e6b6ec10f9f77ec6a016c6cbb9559d1bf) - final logic adjustment for job [ [!29](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/29) [#25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/25) ]
- **automation**: [1f6ee9ea](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1f6ee9ea27824df1c82bf85e1e239f57f2145bdf) - final logic changes [ [!29](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/29) [#25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/25) ]

### Features

- **auto_jobs**: [c5d27e83](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/c5d27e832e100156cb99c5ca580fd5a8eb600e0f) - created initial template to auto-create jobs [ [!29](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/29) [#26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/26) ]
- **variables**: [158cc94d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/158cc94d1a817f89b6603e9bac7678196b21d1d5) - added pipeline trigger and schedule [ [!29](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/29) [#26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/26) ]
- **automation**: [0d3eaa6a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0d3eaa6ac2dc448505b18c6aecd4a72e28ffde83) - job to run ansible playbooks [ [!29](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/29) [!8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/8) [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) [#5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/5) ]

## 0.6.1rc2 (2023-05-24)

### Bug Fixes

- **sub_folder_changelog**: [0482c014](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0482c0144ede393996449a22f1f7742c2e512ac2) - dont create in git submodules [ [!28](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/28) [#23](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/23) ]
- **md_linting**: [e26f590e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e26f590ebcf284be949be4e1d337e1f587755446) - must lint on git tag [ [!27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/27) [!3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/3) ]
- **mkdocs**: [7a9aca3a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7a9aca3a54b1faacb7e286bade84aff0ff4fd2e5) - default to docs directory as root [ [!26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/26) ]
- **template**: [0b9e7375](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0b9e7375c911d65e06b0d801755449ab31cb45ea) - use correct path for build artifact [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **markdown_lint**: [18af7f83](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/18af7f831ad2399a6ae9809c51e87f19450db1a7) - use new lint path [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **markdown_lint**: [12d3a412](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/12d3a412ac73baff16b77488db143efd7311b542) - typo in config variable [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **mkdocs**: [f42b0ecf](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f42b0ecf60def9d0f8d366d09ab91006b6fe32c6) - add placeholder pages [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **docker**: [f604c6e2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f604c6e27d2e7704491f4c78979db40cf89764c0) - ensure qemu binfmt is loaded [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) [!1861](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/1861) ]
- **docker_hub**: [8e0f16c5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8e0f16c585978ded46164c80559b402c0cb2edf2) - push correct image [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) ]
- **lint**: [a754aa81](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a754aa81edf1570b4e8e2e7d4a23025c8b99f314) - use correct path for requirements.txt [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) ]
- **gitlab_release**: [18a28087](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/18a280878799fe077efa0ed5b11bceedd53eb5c8) - allow skip on dev branch [ [!17](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/17) ]

### Code Refactor

- **docs**: [7c385b75](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7c385b7552945699eb87ec3ec43169df0cb77297) - pages dir renamed to docs [ [!26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/26) ]
- **template_website**: [1b59d623](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1b59d62348465cc9cc069d5ee23e759316fa9b3c) - adjust names of jobs [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **markdown_lint**: [bce7396d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/bce7396d8bbf5ec6600a3a34a05198a87c4fcc70) - move md linting to lint folder [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **docs**: [3a2a135d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3a2a135d0af50a9360870e0a7f362c3820543e40) - markdown linting errors fix [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **mkdocs**: [dacb9f22](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/dacb9f22dd9aee1ff741c7ac8078912d9a2b0dbf) - use locked version from website repo [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **docker**: [a90ccb81](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a90ccb81772e295cebe89d7a9c32ab700e19884d) - move docker jobs to their own file [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) ]
- [c34e382a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/c34e382a22cd39874abd8fb5116e831e888db8af) - use name that makes sense [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) ]
- [539e40e3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/539e40e3008e24411f62f439d394db4b5e69a066) - move ansible and yaml lint job to linting folder [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) ]

### Continious Integration

- **pages**: [bcb80358](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/bcb80358d9adb6b3a89fab1003f4434fb2949bdc) - add pages slug [ [!27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/27) ]

### Documentaton / Guides

- [28c04fb2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/28c04fb2e854521167367161d13b09650829d17d) - add job definitions to page [ [!26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/26) ]
- [657df7a5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/657df7a5ceb59798c7bb072aed5bf7ef82aef9b6) - add job definition to page [ [!26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/26) ]
- [0bc3451b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0bc3451bc20e7705a32d89e9f601af363523d946) - added edit url [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- [4fb85408](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4fb85408b8f4e8b87eb97a43db50c86399d8e350) - move readme to project pages index [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- [b66abc19](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b66abc1947676a624d32b4895a9a05000105f36a) - notate under development [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- [61200e52](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/61200e526efcb71bcec9f27ac4bd7c6f02fc23a6) - update structure [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **template**: [e40310fc](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e40310fc21b6af684f6db7858196e8180b6e03df) - add index and website [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- [55061ad5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/55061ad5efd303cf5a53c4672409f7d159113c62) - use project template [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **mkdocs**: [1ec2666e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1ec2666e8565d5206aefaf5462f0f83f74fbbcb7) - moved to pages folder [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **conventional_commits**: [70dfb826](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/70dfb826d100432265e3f3b08948bb808855e0aa) - added config file requirement [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]

### Features

- **template_website**: [bef76847](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/bef76847ec686fcff92229d7b9be0bcfc7b267da) - enable specifying the url slug [ [!27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/27) ]
- **docs**: [a8f675c1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a8f675c102d0027f23b4490aa3620b504d0193cc) - temp adding of requirements [ [!26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/26) ]
- **mkdocs**: [71a335c2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/71a335c2667505c199bd67446327cd8794de5f52) - install website-template requirements [ [!26](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/26) [!7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/7) ]
- **pages**: [480502a7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/480502a7638f346be8334d3c03d5b00ec18f0c2f) - don't include projects in nav [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **template**: [8e2a2338](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8e2a233814bd76ebff3dd8ed5a79afe307a84755) - always deploy to pages on dev manual other [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **mkdocs_build**: [a0b6d05a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a0b6d05a0f3f0fa84c825007f6ec9f28c945f3ef) - always build [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **mkdocs_build**: [6d2e50e9](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6d2e50e947839576f098bd7700e00b9d6ab4be1e) - add manual build [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **template**: [4fa90d4c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4fa90d4c4249ed8929e7dde2e7bd0e8581d0d8a7) - use md lint config from website-template [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **markdown_lint**: [38d46900](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/38d469007a388312c71a61916275d6a12aad8bbd) - enable specifying the lint config path [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **pages**: [15750124](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/157501245d7c347670055352f9263917a2c3f445) - use repo name [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **website**: [16d47d5e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/16d47d5e350e1c78f72c97780ed1732a43927fcc) - add pages job for website [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **template**: [91a50eb1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/91a50eb15bd92ca65481a73c6f095681281941fe) - created website job template [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **mkdocs**: [5556a57e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5556a57ea5588d4f0cd1434bfdde5cd77e3b4f5c) - only run on success [ [!25](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/25) ]
- **conventional_commits**: [088c9fb0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/088c9fb04c80961f4de8d2b129955ae8cd0b9529) - ensure .cz.yaml exists [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) ]
- **docker_build**: [6765894c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6765894cebc958df92fd3f42d93bd205101d1966) - enable spcifying the dockerfile to use [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) ]
- **template**: [67f39d96](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/67f39d9694b80ad0d2d08800d4faadf594fb6623) - added a ansible-role job template [ [!24](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/24) ]
- **gitlab_release**: [d89941df](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d89941df05bfed4b0ad1277e715b224d232e7949) - dont automagic run on dev [ [!4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/4) [#21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/21) [!23](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/23) [#21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/21) [!4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/4) ]

## 0.6.1rc1 (2023-05-15)

### Bug Fixes

- **ci**: [b0024c99](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b0024c99b0cd06e12f95882749b3668a639cf24c) - v no longer suffix to tag [ [!22](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/22) ]
- **docker**: [72f52898](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/72f52898869fe23174e649f0bf8327732fd52147) - setup ROOT_DIR [ [!3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/3) [!1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/1) [!22](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/22) [!3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/3) [!1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/1) ]
- **conventional_commits**: [76db5b17](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/76db5b17578d8585ed31e0728dbfb37ea2fae153) - never run on git tag [ [!7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/7) [!22](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/22) [!7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/7) ]
- **markdown_lint**: [8581981a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8581981a43c31d6903865f067fa3f77adae949e5) - fix search paths [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **yaml_lint**: [a04b272c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a04b272c167dae27940211b7c77a4adcb33b2086) - remove extra var creation [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **yaml_lint**: [3b686a46](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3b686a461be22b682642eb1143f2bd2ea2d3ef17) - ensure config is within double quote [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **yaml_lint**: [52c6ceda](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/52c6ceda83b04e1e18eaa9c32b1a41733dc26497) - scan all [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **yaml_lint**: [0d59871a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0d59871a1a73178c248b2189dfae2cd93f21c469) - enable specifying additional config [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **markdown_lint**: [cf10e289](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/cf10e289d21a5cc529bbe7effb189aab65875510) - enable job for md in sub folders [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) [#19](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/19) [!2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/2) ]
- [d389d141](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d389d14192e1e483fbd48fa9b5c5bee25db14a20) - validation jobs on all except merge [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **gitlab_release**: [a745ceac](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a745ceac5ebce458b46593311e5285f40dcba349) - fixed rule to match nfc_bot [ [!20](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/20) [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) [!20](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/20) ]
- **gitlab_release**: [e76378dd](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e76378dd068e200a1198f1811efb9d3bec7878f5) - only run on master on_success [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) [#16](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/16) ]
- **ci**: [934a401a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/934a401a9620891b09a5fe9c9b0e50a97b43fa9b) - specify the commitizen version [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **markdown_lint**: [8391bf65](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8391bf659bf5dd39edf31205a68c699851e78be3) - remove quotes from search path variable. [ [#18](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/18) ]

### Code Refactor

- **ci**: [02e9e5f4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/02e9e5f4f4cc0b93ae92c7ba3a2cfb38305af64c) - inconsistant tabs [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- [adc720bb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/adc720bbfa0dd8ff66f70fe56678b5f388ce8d0c) - cleanup non-needed dir [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **gitlab_release**: [1fa7fec3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1fa7fec38a54b7ddf460b1394a7024ef161fab24) - show debug before command [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- [408e4eab](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/408e4eab9e1f61004f1e38af6d1531747b7da99b) - move docs as part of restructure [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- [9a7ae710](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9a7ae7106e80a038b31cdc9fc172bb1f974ecb94) - set correct commit details for nfc_bot [ [!20](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/20) ]

### Continious Integration

- [1233d6ad](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1233d6ad90032f3a6c5a3a6ff0c92510d0ef298a) - disable licence scanning until fixed [ [!22](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/22) ]
- **yaml_lint**: [ca60625b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ca60625bf171924e91ea6eea5aa3decc51b7f0dc) - update to python 11
- **markdown_linting**: [47e39849](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/47e3984916bf671e6dbc39e05160a2409fc78b6b) - exclude .gitlab and changelog [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- [49282457](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/492824572b963f048af993fc36d8696f9b0fe41e) - dont lint git submodule website-template [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **docs**: [72f8eb72](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/72f8eb720d5266b7aa83b5e2974da075a1c06875) - added mkdocs config [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]

### Documentaton / Guides

- **yaml_lint**: [a925db14](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a925db14641e709572b832278f43aabe48d153f7) - update docs for new variables [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]

### Features

- **conventional**: [93931cb9](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/93931cb9076e0db238f4e297abe3d8f37bd71b80) - job not to run when bot pushes change [ [!22](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/22) ]
- **ci**: [7ed3f92d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7ed3f92dd75397ad4623ada8469633dc8b0caf5f) - exclude website-template from yaml lint [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **ci**: [bbbf9e35](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/bbbf9e35e2ad5d0fdf1c4c697f127dfe68d5e0da) - set correct search path [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **yaml_lint**: [0b4e85c3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0b4e85c3134ff9f126056113383383559cdfb227) - added var to prevent job from runnng [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **gitlab_release**: [e06ffef6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e06ffef66c4a0ba1f48f109c175239560909e698) - run on merge to development [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **gitlab_release**: [199ea1f2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/199ea1f23c6a3df2b40ae3d9a5668719301500d9) - never run on merge or git tag [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **git_push_mirror**: [1db2209d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1db2209dfb36fbdda28d68388aec9f62f85b57bc) - always sync git tag [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **template**: [8b9a0356](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8b9a0356dec7d99a63c4ed744b78ae707155e9f3) - added new template for ci pipeline for docker containers [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **common**: [9670fc47](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9670fc47401630ef6c407bd7eaccd3db64195543) - created a common ci file for inclusion [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **commit_footer_refs**: [8d512a9a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8d512a9a4bd7f4895645436f057c4bab3efb864e) - ability to disable job with variable [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **gitlab_release**: [a37acbfc](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a37acbfc7d3ea20ece7cb76e15a14858b26f8508) - ability to disable job with variable [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **git_push_mirror**: [81445c06](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/81445c06e43bce10761e3a7fbad7df97f82d6bc2) - ability to disable job with variable [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **conventional_commits**: [9e7d357b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9e7d357bab2b92704d37ad5621df9fe8d1e31a26) - ability to disable job with variable [ [!21](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/21) ]
- **markdown_lint**: [d75e9599](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d75e95998b4a195cfcc36683ffa6f058bf7b05be) - artifact locations to be hard set [ [!19](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/19) ]

## v0.6.1rc0 (2022-01-25)

### Bug Fixes

- **lint_markdown**: [e0402ecf](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e0402ecfb2ab662a74bb70df7937b02576d5e41b) - ensure the correct path for the job directory is used [ [!2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/2) [!18](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/18) ]

## v0.6.0 (2022-01-24)

### Bug Fixes

- **ansible**: [0df60b12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0df60b12dbfff983ca3a671b90ab1be126597e52) - remove duplicate lines that last code review didn't remove.
- **ansible**: [484d9879](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/484d98792a27c9d967331e9d3cd1afdca435bdd6) - fix typo in job pip file
- **dependency_scanning**: [e1894ec0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e1894ec0c4fe7504901682f008c2ff0db7e351fe) - upgraded versions from vulnerability scan.

### Code Refactor

- [6668c2fb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6668c2fb8d7545b4f9052ad3065e58f00d11be62) - test specifying must equal.

### Continious Integration

- **markdown_lint**: [3096d7ee](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3096d7ee0a86d104de04e77b4b734ec0d266020d) - Added Linting of Markdown for files in this repository. [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- **mkdcos**: [a2d705de](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a2d705deb1f3898b6d5fa4d55bd995b1a7ad4b68) - mkdocs requirements.txt had a '\n' in the filename. renamed. [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- **dependency_scanning**: [39a76a08](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/39a76a08691dbdf487405f7c5e6b717eb862d80f) - delete all python 'requirements.txt' files that are not the specified one to be scanned. [ [#350949](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/350949) [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- **dependency_scanning**: [4e1da5e8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4e1da5e87281284e021791a4b600a1bff53b8431) - python 3.7 not available for dependecy scanning. [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- **dependency_scanning**: [a6afa766](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a6afa76600e07d40e8b94fa2d8385ad78634e3b0) - increase python version to 3.7 [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- **dependency_scanning**: [7153f9b4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7153f9b42591e177112d279d2134fc0db1f5a14d) - check python version as pillow 9.0 reported as not found. [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- **dependency_scanning**: [996ee64a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/996ee64ab43f926ca52ab3154ab43e20b6d48fcb) - scanner set to use python 3.6 [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- [725bfaf8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/725bfaf829069002e3b2cb944556d2ce5facb426) - debug logging for dep scanning
- **python_dependency_scan**: [2fffa866](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2fffa866d84f460893c8d9711bc21a74908edb3e) - disabled main job and manual setup for all ci jobs. [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- **licence_finder**: [83cce72a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/83cce72af22b09bd8a245af99e9134d3be129eac) - set to recursive scan so all licence's can be detected.
- **scanners**: [fc816192](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/fc816192be680f64ee1b4b96cccd0d605c529b86) - Added dependency and licence scanners
- [5c872f16](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5c872f163e4de5834efd74a78e3e948d242916ec) - Added a test stage for gitlab specific tests.
- **artifacts**: [e0d8885d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e0d8885d52319a6188c779e80c2064b773721184) - markdown lint and mkdocs build artifacts to expire after 24 hours

### Documentaton / Guides

- **markdown_lint**: [b6dcb47b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b6dcb47b1d1831784d36f482fd99c0ce5e56f088) - removed no longer needed requirement.
- **markdown_lint**: [fd48316a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/fd48316ae763282fc106b7da184c05b35d9ae052) - updated docs on how to use and view rules.
- **mkdocs_build**: [347597e3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/347597e3c1cb20eaa32d1e1cbb2d9d13661a663a) - include mandatory vars in template ci file.
- **mkdocs**: [1ef0e224](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1ef0e2245facffb760ba2ad9a57af1d6178a2d1a) - Completed the mkdocs build readme [ [#15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/15) [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) ]
- **markdown_lint**: [6363ea37](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6363ea377cd008bbc839e6f4ee4fca337b77bc19) - completed the job docs. [ [#12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/12) ]
- **mkdocs**: [5c05ed76](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5c05ed7605ddbecb1a3c7046716afa07829c264f) - initial adding of mkdocs build readme. [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) [#5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/5) ]
- **markdown_lint**: [6383cde3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6383cde3bf9985b2cb43908bc2486d1dc67b7026) - initial adding of the docs [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) [#12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/12) ]

### Features

- **markdown_lint**: [9ab336fb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9ab336fbddd6cba1d29c5a001ab52772ed4554b6) - include junit configuration file '.markdownlint-cli2.jsonc' in ci job.
- **mkdocs_build**: [906f09e2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/906f09e2d3285681bd982d65eda3f56cf5a5169e) - use a pip file for job so that licence scanning can function.
- **mkdocs_build**: [5a41962a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5a41962a994a54d99a3e7ab1bc0d7379ea14c1c2) - move ci job dependencies to a pip file so that the ci dependency job can check versions.
- **build**: [50b5e854](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/50b5e8542b827e6b6cf70f3f4c26b4c1737fe0c1) - initial add of mkdocs build job [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) [#15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/15) ]
- **validation**: [954aa28d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/954aa28dbf1073be05a3dd6d13da818a0bc7cb4e) - Added a Markdown linting validation job. [ [!15](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/15) [#12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/12) ]

## v0.5.0 (2022-01-16)

### Bug Fixes

- **commit.py**: [73918f2f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/73918f2f5e19440d0e300da3a20712739c316d88) - filter merge request search to 'opened' and on current branch. [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!13](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/13) ]

### Continious Integration

- **MR_Title**: [31517b4b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/31517b4bf00c1f177ef925d09b1a6714577f62c5) - save the merge request title as a variable and debug output in job log. [ [!13](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/13) ]

### Documentaton / Guides

- **README.md**: [f4670844](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f4670844cc0961bf38fbf760f8eee505a54ab495) - Added project header template [ [!13](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/13) ]

### Features

- **.yaml_lint_defaults**: [140985c3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/140985c3a4ea07cf30f7fe8c970fb07cc61b776d) - Always run on all branches as this denotes quality. [ [!13](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/13) ]
- **commit_footer_refs**: [82c6c9f5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/82c6c9f5d53594544cea9a7bc59a10ab1e9ebedd) - never run on development or master. [ [!13](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/13) ]

## v0.4.0 (2022-01-15)

### Bug Fixes

- **commit.py**: [99bdc2a0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/99bdc2a0929d4e7036e50e8ce22ce9b0f90f0736) - fix typo that caused exception [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **conventional_commits**: [d03d9fef](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d03d9fefc916dd6730d9ffa778c11d48d621318e) - fetch all branches prior to check for parent branch [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **ci**: [d5782d95](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d5782d95e825d406ea805c425cfefd6752fb6e35) - added variable 'GIT_SUBMODULE_STRATEGY' to be 'recursive' [ [#10](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/10) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **conventional_commits**: [42ad02ee](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/42ad02ee5db65c3c6c33ad14fe0371c9916897bf) - use git show-branch to find origin branch [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/11) ]

### Features

- **commit.py**: [e5531fc7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e5531fc77b5bdb1ccc0741e388df2d8d25ba6ade) - throw an error if no token was supplied. i.e. empty variable. [ [#11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/11) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **commit.py**: [6b7ad95f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6b7ad95fc0ccccf79ff645bad3f86660f5096a4e) - confirm a merge request was found, if not output 'ci: No Merge Request found' [ [#11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/11) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **commit.py**: [c543c47a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/c543c47af8c7c386ae57f5a7a50904d396758c3a) - try to us `CI_JOB_TOKEN` before the specified token, if any. [ [#11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/11) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **commit.py**: [b01550e0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b01550e09f273edc8a57f4ad4b41ee2d67705d41) - removed ability to fetch first commit or target branch [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]

## v0.3.1 (2022-01-11)

### Bug Fixes

- **pylint**: [4b6cc317](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4b6cc3176fc4acc3b7dbb954162802af9cbb4c68) - install the required packages for files being checked [ [#7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/7) ]
- **pylint**: [936299ae](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/936299aefc6eadf9cbfec3152b352b321969cfab) - fix bug introduced in code quality commit [ [#7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/7) ]
- **commit_footer**: [2ac22c0e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2ac22c0e914016a8944ff9b94640f3e87f409069) - fix bug introduced in code quality commit [ [#7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/7) ]

### Documentaton / Guides

- **readme**: [8ac36de8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8ac36de8e0f113ce17d54dfce1345a0adab41bc8) - Updated with an example .gitlab-ci.yml example [ [#2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/2) [!10](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/10) ]

## v0.3.0 (2021-08-12)

### BREAKING CHANGE

- !2

### Bug Fixes

- **commit_message**: [3360a15f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3360a15fde12682edfd9044d2541dc819615b838) - fixed commit message check if there is only one commit to the branch [ [!7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/7) ]
- **commit_footer_refs**: [63af1efb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/63af1efb4fd92a9f8755f766728a18d8f390b805) - Use the current git branch for comparison. [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [f76cabee](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f76cabeeb04b028a231dc1c232862db5fcad4345) - Adjust release workflow [ [!2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/2) ]

### Code Refactor

- **gitlab_release**: [eb0bf4c1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/eb0bf4c1740dbd7a47ceb031c0d1c854899a1e40) - file link to be in local repository for helping fix commit footer ref check failures [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]
- **gitlab_release**: [81776223](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/81776223c5cb392c12c7ca63488a1df10290e9d1) - use a name for failed test to denote the issue [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]

### Continious Integration

- **gitlab_release**: [7cb676eb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7cb676eb98a7de30d47a6b49a87067116684cfd2) - Add a validation job to check if commit messages contain a gitlab reference in the footer [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]

### Documentaton / Guides

- **readme**: [0653766c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0653766c935cb117082bfe1481ae83e4a1b2bb5c) - Updated badges and intro [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) ]
- **gitlab_templates**: [9f7a24c1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9f7a24c1ebc0bdb5a153977dcb1c53d7ec2fb140) - added issue and merge request templates [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **template**: [da8eb5c3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/da8eb5c3381379f6e405c3ebe14d9a883c52f41a) - added template readme for CI job folders [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **readme**: [ace7a034](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ace7a03456861d59e2f904405f45409c53e831ab) - explain sync and using github to link gitlab-ci [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **readme**: [8790917e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8790917e7d959aa7b8305912bb443ba6b72200c6) - explain repo layout and versioning [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) ]
- **readme**: [19900945](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/19900945e763249b6ef7a9e2e2cbcf11748b1eea) - added how to update gitlab-ci [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) ]
- **readme**: [8a988ebf](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8a988ebf09015211f8f6566acc0ba71c1f00bee1) - Added how to use this repository [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) ]
- **gitlab_release**: [dc13d4f2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/dc13d4f2841038c085dcf29dfb0b0c5d2f00f099) - Added user docs to fix errors from ci job 'commit footer refs' [ [#3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/3) [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]
- **changelog**: [35edb7cf](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/35edb7cfc59e2d147bdb5cb5d03710ec747073ae) - Updated changelog to new layout [ [!3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/3) [#3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/3) ]
- **gitlab_release**: [5f273ce2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5f273ce23a331eaf11623207ec4aba8b856c14f0) - Updated docs with new instructions on version incrementing [ [!2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/2) ]

### Features

- **python_linting**: [d6105624](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d61056243804728e059b99fce1644a8cc37230bb) - added ci job, python linting, code quality and scoring [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **yaml_lint**: [d20a56fa](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d20a56fa0ca492e3fc2ad7c548fc891cc8ffc8ec) - Added job yaml lint for checking yaml files [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [22136f7d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/22136f7dd22b9487d362a7ed63ca1b76e52b9cc7) - Toggle var added to enable switching changelog references. [ [#3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/3) ]
- **gitlab_release**: [756b9406](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/756b9406dde8cf0bf0030ac72855a054ece3a883) - be able to toggle commit footer check job [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]
- **gitlab_release**: [11e15661](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/11e156619d0d820e534897bafd5f39e6f9defcbf) - python module to check if a commit message has gitlab references in the footer [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]
- **gitlab_release**: [8699c412](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8699c41219d70e6f41f42dc7f2c1bcf542b3f723) - Add commit footer to changelog [ [!1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/1) [#3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/3) ]

## v0.3.0rc1 (2021-08-04)

### Documentaton / Guides

- **changelog**: [cb78ab82](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/cb78ab82182a9edcd568a8b4c315490041539149) - regenerated so that all entries use the new url format [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

## v0.3.0rc0 (2021-08-04)

### Code Refactor

- **gitlab_release**: [cc3fabda](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/cc3fabdaa28f97c3e1600e4a0d95a05bb547e772) - Use Short commit SHA1 in main changelog link to gitlab [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Features

- **gitlab_release**: [3e8c3ce7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3e8c3ce7cd64a6e9110818d32c15c3602fefb76c) - On the development brnach, releases to be 'rc' to denote considered non-stable [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

## v0.2.1 (2021-08-04)

### Bug Fixes

- **gitlab_release**: [588698df](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/588698df2668853a97fe60901ab324310f34f279) - Correctly fetch the CI_PROJECT_URL for the environment

## v0.2.0 (2021-08-04)

### Code Refactor

- **gitlab_release**: [7a69685b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7a69685b53cbe5bd7341a176bf63fd17d36bc7f0) - Dont conduct any release, git push or tag delete if the version was not bumped
- **gitlab_release**: [72e8b6c8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/72e8b6c84defdb903c5741e3469651987769713f) - build gitlab commit url for changelog so that there is a weblink to the changes [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Documentaton / Guides

- **gitlab_release**: [eebe8e30](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/eebe8e30dcb11cd239f35fcb98216b2ae4d20ece) - Include custom command instructions [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Features

- **gitlab_release**: [287b4c95](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/287b4c954dddfaaf0a66af387676ea438cc80e61) - Include code refactor as part of the changelog [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

## v0.1.0 (2021-08-04)

### Bug Fixes

- **gitlab_release**: [80ca3618](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/80ca3618ee56d0f2a2c012416cb6206599a4f3f6) - A 'feat' commit must do a MINOR bump to version [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [ed5be7fd](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ed5be7fd3c16e86d48e179a2cded53a38f79e1d9) - ci image is alpine, use '/bin/sh' and add the changlogs to git cache for commiting [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [7706085b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7706085b09f3cd9b7c09f7f93b182fd425f6525a) - All tasks run as part of script including user custom script [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [1446c28e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1446c28ed2bfe2efec99bc2fc83b111717bcb2af) - Use a user token to access the git repo for pushing commits back [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **ansible**: [2a3266fb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2a3266fb537e22dddf47708d0af101945027128f) - Ensure the default ci directory is populated [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Code Refactor

- **gitlab_release**: [2035ed27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2035ed27af7fc1f3f5b2c42aa5874219fc5fe323) - use 'git log' to get current commit hash [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Continious Integration

- **git_push_mirror**: [b5935056](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b593505698b3d3359569f29f97c90e17e211f304) - Push repo to github NoFussComputing/gitlab-gi [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **conventional_commits**: [a2174104](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a2174104d1eb05d329bacd44700bf81ac709dcac) - Add conventional commits job to check commits and MR titles [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Documentaton / Guides

- **README.md**: [247264e3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/247264e36bc0b6c86d2f06f8dae09ff7447fc156) - Added readme for the repo [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **git_push_mirror**: [7ffb2041](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7ffb20418cfa8e6fa20cca60e42155171961d1ce) - Update workflow and typos [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Features

- **job_changelog**: [1ecd857c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1ecd857c0bf8ef009ad2482ad1d52604adadc0ed) - Create a changelog per job folder [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **git_release**: [6678a3db](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6678a3dbab2763addc185e766cbaffbc074a6e98) - Migrated from ansible-roles [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **ansible**: [2413daef](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2413daefb1e7e5a9e7a3cbb2d8cff2214f4a98ae) - Added ansible validation job for linting [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **git_push_mirror**: [9b28ae59](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9b28ae5952adfb3d61e660814074ad3c7b42ff61) - Added a job that syncs to a remote git repo [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **conventional_commits**: [392a200f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/392a200fd469c4161dbab5f2b59031a7a64f20a2) - Added conventional commit job [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

## v0.0.1 (2021-08-03)
