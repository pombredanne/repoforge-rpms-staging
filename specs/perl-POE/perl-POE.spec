# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$pobox,com>

# ExcludeDist: el2 rh7 rh8 rh9 el3

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE

Summary: Portable multitasking and networking framework for Perl
Name: perl-POE
Version: 0.3003
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cpan.org/modules/by-module/POE/POE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Provides: perl(POE::Resource::Controls)

%description
POE is a networking and multitasking (some say cooperative threading)
framework for Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	--default \
        destdir="%{buildroot}%{_prefix}" \
        INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES TODO HISTORY
%doc %{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.3003-1
- Initial package.
