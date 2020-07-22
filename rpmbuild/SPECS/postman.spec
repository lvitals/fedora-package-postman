%define debug_package %{nil}

Name:    postman
Version: 7.28.0
Release: 1%{?dist}
Summary: Postman is the essential toolchain for API developers to share, test, document and monitor APIs.
License: Copyright (c) 2013-2016 GitHub Inc.
URL:     https://www.getpostman.com/
Source0: https://dl.pstmn.io/download/version/%{version}/linux64
Source1: %{name}.desktop

AutoReqProv: no

ExclusiveArch: x86_64

%description
Postman is the essential toolchain for API developers to share, test, document and monitor APIs. More than 3 million engineers and developers worldwide use Postman to build connected software via APIs—quickly, easily and accurately. Postman's free Mac, Windows, Linux and Chrome apps, along with Postman's paid Pro and Enterprise offerings, are standards at industry leading businesses. Postman has offices in San Francisco, Bangalore, and Austin, and is privately held, with funding from Nexus Venture Partners.

%prep
%setup -q -n Postman

# fix permissions
find . -type d -exec chmod 0755 {} ";"
find . -type f -exec chmod 0644 {} ";"
chmod 755 Postman

%build
rm -rf %{buildroot}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications %{buildroot}/opt/%{name}
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps

install -D -m 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

cp -r * %{buildroot}/opt/%{name}
cp %{_builddir}/Postman/app/resources/app/assets/icon.png  %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

ln -sfn /opt/%{name}/Postman %{buildroot}%{_bindir}/%{name}

chmod +x %{buildroot}/opt/%{name}/app/_Postman

%post
gtk-update-icon-cache /usr/share/icons/hicolor

%postun
gtk-update-icon-cache /usr/share/icons/hicolor

%files
%defattr(-,root,root)
#%license LICENSE
#%doc version
/opt/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Wed Jul 22 2020 Leandro Vital <leandro.santos@ima.sp.gov.br>
- initial package
