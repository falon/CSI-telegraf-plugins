Name:		CSI-telegraf-plugins
Version:	0.1
Release:	8%{?dist}
Summary:	external agents for collecting, processing, aggregating, and writing metrics for Telegraf.

Group:		Development/Tools
License:	MIT
URL:		https://github.com/falon/telegraf-plugins
Source0:	https://github.com/falon/telegraf-plugins/archive/refs/heads/master.zip

BuildRequires:	go
BuildRequires:  systemd-devel
BuildRequires:  unzip
Requires:       systemd
Requires:	telegraf > 1.20.2

Vendor:		Falon Entertainment
Packager:	Marco Favero <marco.favero@csi.it>


%description
This is a collection of external plugins for Telegraf.
These input plugins are currently included:
- ds389: we hope will be soon part of Telegraf
- ldap_org: measure number of entries per organization tree


%prep
spectool -R -f -g %{_topdir}/SPECS/Telegraf-plugin.spec
%autosetup -n %{name}-master


%build
go build -ldflags="-linkmode=external -compressdwarf=false" -o telegraf-ds389 cmd/main-ds389.go
go build -ldflags="-linkmode=external -compressdwarf=false" -o telegraf-ldap_org cmd/main-ldap_org.go

%install
install -D -m 0750 -t %{buildroot}%{_bindir} telegraf-*
install -D -m 0644 -t %{buildroot}%{_sysconfdir}/%name *.conf
install -D -m 0644 plugins/inputs/ds389/README.md README-ds389.md
install -D -m 0644 plugins/inputs/ldap_org/README.md README-ldap_org.md

%files
%doc README*.md 
%attr(-, root, telegraf) %_bindir/telegraf-ds389
%attr(-, root, telegraf) %config(noreplace) %_sysconfdir/%name/ds389.conf
%attr(-, root, telegraf) %_bindir/telegraf-ldap_org
%attr(-, root, telegraf) %config(noreplace) %_sysconfdir/%name/ldap_org.conf



%changelog
* Wed Nov 10 2021 Marco Favero <m.faverof@gmail.com> - 0.1.8
- Added a limited set of returned metrics by suffix.
* Wed Nov 10 2021 Marco Favero <m.faverof@gmail.com> - 0.1.7
- Added Locks monitor in DB transactions.
* Tue Nov 09 2021 Marco Favero <m.faverof@gmail.com> - 0.1.6
- added some metrics about DB transactions.
* Mon Nov 08 2021 Marco Favero <m.faverof@gmail.com> - 0.1-5
- added normalized dn cache metrics.
* Wed Nov 03 2021 Marco Favero <m.faverof@gmail.com> - 0.1-4
- added threads and nbackends as metric.
- added "starttime" and "currenttime" to tags.
* Mon Apr 26 2021 Marco Favero <m.faverof@gmail.com> - 0.1-3
- Fixed ownership
* Mon Apr 19 2021 Marco Favero <m.faverof@gmail.com> - 0.1-1
- Initial Release

