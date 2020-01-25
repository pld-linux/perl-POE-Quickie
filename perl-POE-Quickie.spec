#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	POE
%define		pnam	Quickie
Summary:	POE::Quickie - A lazy way to wrap blocking code and programs
#Summary(pl.UTF-8):
Name:		perl-POE-Quickie
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a510c905e4bc84fb945ab0a2d85dfd16
URL:		http://search.cpan.org/dist/POE-Quickie/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Capture::Tiny) >= 0.07
BuildRequires:	perl-POE >= 1.291
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you need nonblocking access to an external program, or want to
execute some blocking code in a separate process, but you don't want
to write a wrapper module or some POE::Wheel::Run boilerplate code,
then POE::Quickie can help. You just specify what you're interested in
(stdout, stderr, and/or exit code), and POE::Quickie will handle the
rest in a sensible way.

It has some convenience features, such as killing processes after a
timeout, and storing process-specific context information which will
be delivered with every event.

There is also an even lazier API which suspends the execution of your
event handler and gives control back to POE while your task is
running, the same way LWP::UserAgent::POE does. This is provided by
the quickie_* functions which are exported by default.

# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/*.pm
%{_mandir}/man3/*
