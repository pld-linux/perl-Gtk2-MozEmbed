#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
%bcond_without	dom	# DOM feature
#
%define		pnam	Gtk2-MozEmbed
Summary:	Gtk2::MozEmbed - Mozilla embedding in Perl
Summary(pl.UTF-8):	Gtk2::MozEmbed - osadzanie Mozilli w Perlu
Name:		perl-Gtk2-MozEmbed
Version:	0.11
Release:	0.1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	8f5a2b918e4784b87370b0225ae551e8
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.200
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
%{?with_dom:BuildRequires:	perl-Mozilla-DOM >= 0.01}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Glib-devel >= 1.180
BuildRequires:	perl-Gtk2-devel >= 1.081
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	xulrunner-devel >= 1.8
# needs gtkmozembed API
BuildRequires:	xulrunner-devel < 2:2.2
Requires:	perl-Glib >= 1.180
Requires:	perl-Gtk2 >= 1.081
%{?with_dom:Requires:	perl-Mozilla-DOM >= 0.01}
%requires_eq	xulrunner-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	libgtkembedmoz.so libxpcom.so

%description
This module allows you to use the Mozilla embedding widget from Perl.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Ten moduł pozwala używanie widgetu osadzającego Mozillę z poziomu
Perla.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gtk2-MozEmbed bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gtk2-MozEmbed dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.120
Requires:	perl-Gtk2-devel >= 1.121
Requires:	xulrunner-devel >= 1.8

%description devel
Development files for Perl Gtk2-MozEmbed bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gtk2-MozEmbed dla Perla.

%prep
%setup -q -n %{pnam}-%{version}

# rely only on bcond setting
%{__sed} -i -e '/^my \$use_dom/ s/1/%{with dom}/' Makefile.PL
%{__sed} -i -e '/^unless.*use Mozilla::DOM/,/^}/ d' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/MozEmbed/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.pre-git NEWS README
%{perl_vendorarch}/Gtk2/MozEmbed.pm
%dir %{perl_vendorarch}/Gtk2/MozEmbed
%dir %{perl_vendorarch}/auto/Gtk2/MozEmbed
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/MozEmbed/MozEmbed.so
%{_mandir}/man3/Gtk2::MozEmbed*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/MozEmbed/Install
