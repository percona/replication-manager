%global majorversion 1
%global minorversion 0

Summary:        Replication manager for PXC and MariaDB
Name:           percona-replication-manager
Version:        %{majorversion}.%{minorversion}
Release:        1%{?dist}
License:        GPLv3
Group:          Applications/Databases
URL:            https://github.com/percona/replication-manager
Packager:       Percona Development Team <https://jira.percona.com>
Vendor:         Percona, LLC
BuildArch:      x86_64
Source0:        %{name}-%{version}.tar.gz

Requires:       percona-xtradb-cluster-client

%description
Replication manager for PXC and MariaDB
The typical use case would be to manager a master-master replication link between two distincts PXC clusters but the tools supports more complex topology.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} -p -D -m 0755 replication_manager.sh %{buildroot}%{_bindir}/replication_manager.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/replication_manager.sh

%changelog
* Thu Dec 15 2022 Surabhi Bhat <surabhi.bhat> 1.0-1
- Initial build for percona-replication-manager
