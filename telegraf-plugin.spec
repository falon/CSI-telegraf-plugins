Name:		CSI-telegraf-plugins
Version:	0.1
Release:	1%{?dist}
Summary:	external agents for collecting, processing, aggregating, and writing metrics for Telegraf.

Group:		Development/Tools
License:	MIT
URL:		https://github.com/falon/telegraf-plugins
Source0:	https://github.com/falon/telegraf-plugins/archive/refs/heads/master.zip

BuildRequires:	go
BuildRequires:  systemd-devel
BuildRequires:  unzip
Requires:       systemd
Requires:	telegraf > 1.18.0

Vendor:		Falon Entertainment
Packager:	Marco Favero <marco.favero@csi.it>


%description
This is a collection of external plugins for Telegraf.
These input plugins are currently included:
- ds389: we hope will be soon part of Telegraf
- ldap_org: measure number of entries per organization tree


%prep
spectool -R -f -g %{_topdir}/SPECS/telegraf-plugin.spec
%autosetup -n %{name}-master


%build
go build -ldflags="-linkmode=external -compressdwarf=false" -o telegraf-ds389 cmd/main-ds389.go
go build -ldflags="-linkmode=external -compressdwarf=false" -o telegraf-ldap_org cmd/main-ldap_org.go

%install
install -D -m 0750 -t %{buildroot}%{_bindir} -g telegraf telegraf-*
install -D -m 0644 -t %{buildroot}%{_sysconfdir}/%name -g telegraf *.conf
install -D -m 0644 plugins/inputs/ds389/README.md README-ds389.md
install -D -m 0644 plugins/inputs/ldap_org/README.md README-ldap_org.md

%files
%doc README*.md 
%_bindir/telegraf-ds389
%config(noreplace) %_sysconfdir/%name/ds389.conf
%_bindir/telegraf-ldap_org
%config(noreplace) %_sysconfdir/%name/ldap_org.conf



%changelog
* Mon Apr 19 2021 Marco Favero <m.faverof@gmailcom> - 0.1-1
- Initial Release

