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

%package -n     vscodium-nautilus
Summary:        VS Codium extension for Nautilus
Requires:       nautilus-python%{?_isa}

%description -n vscodium-nautilus
This extension adds 'Open VS Codium' item to right click context menu in Nautilus.

%prep
%autosetup

%install
install -D -m 644 open-vscode.py %{buildroot}%{_datadir}/nautilus-python/extensions/open-vscode.py
install -D -m 644 open-vscode.py %{buildroot}%{_datadir}/nautilus-python/extensions/open-vscodium.py
sed -i "s/BINARY = 'code'/BINARY = 'codium'/g" %{buildroot}%{_datadir}/nautilus-python/extensions/open-vscodium.py
sed -i "s/NAME = 'VS Code'/NAME = 'VS Codium'/g" %{buildroot}%{_datadir}/nautilus-python/extensions/open-vscodium.py
sed -i "s/class OpenVSCodeExtension/class OpenVSCodiumExtension/g" %{buildroot}%{_datadir}/nautilus-python/extensions/open-vscodium.py

%files
%{_datadir}/nautilus-python/extensions/open-vscode.py*

%files -n vscodium-nautilus
%{_datadir}/nautilus-python/extensions/open-vscodium.py*

%changelog
* Thu Dec 12 2019 Lukas Brabec <lbrabec@redhat.com> - 1.1-1
- added subpackage for VS Codium

* Wed Dec 11 2019 Lukas Brabec <lbrabec@redhat.com> - 1.0-1
- initial packaging