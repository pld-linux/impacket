Summary:	Network protocols Constructors and Dissectors
Summary(pl):	Konstruktory i analizatory dla protoko��w sieciowych
Name:		impacket
Version:	0.9.4
Release:	0.1
License:	Apache Software License 1.1
Group:		Libraries
Source0:	http://oss.coresecurity.com/repo/Impacket-%{version}.tar.gz
# Source0-md5:	83e742d5c664ba91af78617123435dd1
URL:		http://oss.coresecurity.com/projects/impacket.html
BuildRequires:	python-devel >= 2.2.1
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Impacket is a collection of Python classes for working with network
protocols. Impacket is mostly focused on providing low-level
programmatic access to the packets, however some protocols (for
instance NMB and SMB) are implemented in a higher level as a
foundation for other protocols. Packets can be constructed from
scratch, as well as parsed from raw data, and the object oriented API
makes it simple to work with deep hierarchies of protocols.

Impacket is most useful when used together with a packet capture
utility or package such as Pcapy, an object oriented Python extension
for capturing network packets.

%description -l pl
Impacket to zbi�r klas Pythona do pracy z protoko�ami sieciowymi.
Impacket w wi�kszo�ci skupia si� na zapewnieniu niskopoziomowego
dost�pu z poziomu programu do pakiet�w, chocia� niekt�re protoko�y
(jak na przyk�ad NMD i SMB) s� zaimplementowane na wy�szym poziomie
jako podstawa dla innych protoko��w. Pakiety mog� by� konstruowane od
zera, a tak�e z surowych danych, a obiektowo zorientowane API u�atwia
prac� z g��bokimi hierarchiami protoko��w.

Impacket jest najbardziej przydatny przy u�ywaniu wraz z narz�dziem do
przechwytywania pakiet�w lub pakietem takim jak Pcapy, kt�ry jest
obiektowo zorientowanym rozszerzeniem Pythona do przechwytywania
pakiet�w sieciowych.

%prep
%setup -q -n Impacket-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/impacket
%dir %{py_sitedir}/impacket/dcerpc
%{py_sitedir}/impacket/*.py[co]
%{py_sitedir}/impacket/dcerpc/*.py[co]
%{_examplesdir}/%{name}-%{version}
