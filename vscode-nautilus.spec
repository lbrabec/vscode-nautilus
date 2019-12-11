Name:           vscode-nautilus
Version:        1.0
Release:        1%{?dist}
Summary:        Visual Studio Code extension for Nautilus

License:        MPLv2.0
URL:            https://github.com/lbrabec/vscode-nautilus
Source0:        https://github.com/lbrabec/vscode-nautilus/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       nautilus-python%{?_isa}

%description
This extension adds 'Open VS Code' item to right click context menu in Nautilus.

%prep
%autosetup

%install
install -D -m 644 open-vscode.py %{buildroot}%{_datadir}/nautilus-python/extensions/open-vscode.py

%files
%{_datadir}/nautilus-python/extensions/open-vscode.py*

%changelog
* Wed Dec 11 2019 Lukas Brabec <lbrabec@redhat.com> - 1.0-1
- initial packaging