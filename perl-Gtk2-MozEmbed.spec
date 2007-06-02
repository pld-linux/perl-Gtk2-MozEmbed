#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gtk2-MozEmbed
Summary:	Gtk2::MozEmbed - Mozilla embedding in Perl
Summary(pl.UTF-8):	Gtk2::MozEmbed - osadzanie Mozilli w Perlu
Name:		perl-Gtk2-MozEmbed
Version:	0.06
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	4ee3b09c640d66a66640ec65cd30c36a
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	perl-ExtUtils-Depends >= 0.200
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
#BuildRequires:	perl-Mozilla-DOM >= 0.01
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Glib >= 1.060
BuildRequires:	perl-Gtk2 >= 1.081
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	xulrunner-devel >= 1.8
Requires:	libgtkhtml >= 2.0.0
Requires:	perl-Glib >= 1.060
Requires:	perl-Gtk2 >= 1.081
#Requires:	perl-Mozilla-DOM >= 0.01
Requires:	xulrunner-libs >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to use the Mozilla embedding widget from Perl.

%description -l pl.UTF-8
Ten moduł pozwala używanie widgetu osadzającego Mozillę z poziomu
Perla.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/MozEmbed/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%{perl_vendorarch}/Gtk2/MozEmbed.pm
%dir %{perl_vendorarch}/Gtk2/MozEmbed
%{perl_vendorarch}/Gtk2/MozEmbed/Install
%dir %{perl_vendorarch}/auto/Gtk2/MozEmbed
%{perl_vendorarch}/auto/Gtk2/MozEmbed/MozEmbed.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/MozEmbed/MozEmbed.so
%{_mandir}/man3/Gtk2::MozEmbed*.3pm*
