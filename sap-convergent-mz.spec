#
# spec file for package sap-convergent-mz
#
# Copyright (c) 2023-2024 SUSE LLC
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

Name:           sap-convergent-m
Version:        0.3.5
Release:        0
Group:          Productivity/Clustering/HA
Summary:        Resource agents to control the convergent mediation control zone
# Selected GPL-2.0-or-later as correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-2.0-or-later 
URL:            https://www.suse.com 
Source0:        %{name}-%{version}.tgz 

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       pacemaker > 2.1.2
Requires:       resource-agents
Requires:       python3
Requires:       /usr/bin/xmllint

%description
mz shell simulator not to be used for production, only for internal development

Authors:
--------
    Fabian Herschel
    Lars Pinne


%prep
tar xf %{S:0}

%install

mkdir -p %{buildroot}/usr/bin
install -m 0755 test/bin/mzsh %{buildroot}/usr/bin

%files
%defattr(-,root,root)
/usr/bin/mzsh

%changelog
