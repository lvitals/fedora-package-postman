# fedora-package-postman

Package: Postman

Version: 7.28

Arch: x86_64


### Configurition

```bash

$ sudo dnf install fedora-packager @development-tools

$ sudo usermod -a -G mock <your username>

$ cp -R rpmbuild cd ~/

$ cd ~/rpmbuild/SOURCES

$ wget https://dl.pstmn.io/download/version/7.28/linux64

$ cd ~/rpmbuild/SPECS

$ rpmbuild -ba postman.spec

```


### Build

```bash

$ cd ~/rpmbuild/SPECS

$ rpmbuild -ba postman.spec

```

### Install

```bash

$ cd ~/rpmbuild/RPMS/x86_64

$ sudo rpm -U postman-7.28.0-1.fc32.x86_64.rpm

```



