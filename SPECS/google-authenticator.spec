%define checkout 20150913
%define gh_commit 1d4d95014e57eb68b874021c84e781d1010b0165
%define gh_short %(c=%{gh_commit}; echo ${c:0:7})
%define gh_owner sebastianbergmann
%define gh_project php-token-stream


Name:           google-authenticator
Version:        1.01
Release:        1.%{checkout}git%{gh_short}%{?dist}
Summary:        One-time passcode support using open standards

License:        ASL 2.0
URL:            https://github.com/google/google-authenticator/
Source0:        https://github.com/google/google-authenticator/archive/%{gh_commit}.zip
BuildRequires:  pam-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
The Google Authenticator package contains a pluggable authentication
module (PAM) which allows login using one-time passcodes conforming to
the open standards developed by the Initiative for Open Authentication
(OATH) (which is unrelated to OAuth).

Passcode generators are available (separately) for several mobile
platforms.

These implementations support the HMAC-Based One-time Password (HOTP)
algorithm specified in RFC 4226 and the Time-based One-time Password
(TOTP) algorithm currently in draft.

%prep
%setup -q -n google-authenticator-%{gh_commit}

%build
cd libpam
./bootstrap.sh
%configure
# https://github.com/google/google-authenticator/issues/517
sed -i 's/^#define PAM_CONST .*/#define PAM_CONST const/' config.h
make %{?_smp_mflags}

%check
cd libpam
make check

%install
rm -rf %{buildroot} # redundant except for RHEL 5
cd libpam
%make_install

%files
/%{_usr}/%{_lib}/security/*
%{_bindir}/google-authenticator
%docdir %{_docdir}/%{name}
%{_docdir}/%{name}/*


%changelog
* Sun Sep 13 2015 mh <mh@immerda.ch> - 1.01-1.201509133gitab72c62
- Initial Version
