#
# spec file for package sap-convergent-ha
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           sap-convergent-ha
Version:        0.0.1
Release:        0
Group:          Productivity/Clustering/HA
Summary:        Resource agents to control the convergent mediation control zone
# Selected GPL-2.0-or-later as correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-2.0-or-later 
URL:             
Source0:         %{name}-%{version}.tgz 
BuildRequires:  
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       pacemaker > 2.1.2
Requires:       resource-agents
Requires:       python3
Requires:       /usr/bin/xmllint

%description
Resource agents to control the convergent mediation control zone. The used interface to the application is the mz-shell.

Authors:
--------
    Fabian Herschel
    Lars Pinne


%prep
tar xf %{S:0}
#%autosetup

%build
gzip man/*
#%configure
#%make_build

%install
#%make_install

# resource agents (ra)
mkdir -p %{buildroot}/usr/lib/ocf/resource.d/suse
install -m 0755 ra/SAPHana* %{buildroot}/usr/lib/ocf/resource.d/suse/

# manual pages
mkdir -p %{buildroot}%{_mandir}/man7
install -m 0444 man/*.7.gz %{buildroot}%{_mandir}/man7

%post
%postun

%files
%dir /usr/lib/ocf/resource.d/suse
/usr/lib/ocf/resource.d/suse/*
#/usr/share/%{name}
#%dir /usr/lib/%{name}

%license COPYING
%doc README
#%doc ChangeLog README
%doc %{_mandir}/man7/*

%changelog

