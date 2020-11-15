Name:           h2b2
Version:        2
Release:        0
Summary:        hex to binary

Group:          jpegleg
License:        MIT
URL:            https://github.com/jpegleg/h2b2
Source0:        h2b2_latest_qa.tgz

%description
Pipe hex into h2b2 and get binary out. 

%prep
%build
%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install -m 0755 SOURCES/h2b2 $RPM_BUILD_ROOT/usr/local/bin/
cp SOURCES/h2b2 /usr/local/bin/

%files
/usr/local/bin/h2b2

%changelog
* Sun Nov 15 2020 Keegan Bowen  2.0.0
  - starting packaging for rpm
