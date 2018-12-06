# https://github.com/google/go-github
%global goipath github.com/google/go-github

%global common_description %{expand:
go-github is a Go client library for accessing the GitHub API v3.}

Version:        18.2.0

%gometa

# gometa strips the leading "go-" off the name
%global goname golang-github-google-go-github

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for accessing the GitHub API
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%package devel
Summary:       %{summary}

BuildRequires: mailcap
BuildRequires: golang(github.com/google/go-querystring/query)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(google.golang.org/appengine)
BuildRequires: golang(google.golang.org/appengine/log)

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
# Remove network tests that talk to the live Github API.
rm -rf test
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS CONTRIBUTING.md example


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 18.2.0-1
- Update to official v18.2.0 release

* Thu Jul 26 2018 Ed Marshall <esm@logic.net> - 15.0.0-5
- Switch to forge-specific packaging.
- Fix test failures with go 1.11.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Ed Marshall <esm@logic.net> - 15.0.0-2
- Update BuildRequires to match newest version.

* Sat Feb 03 2018 Ed Marshall <esm@logic.net> - 15.0.0-1
- Update to official v15.0.0 release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git553fda4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git553fda4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Ed Marshall <esm@logic.net> - 0-0.1.git553fda4
- First package for Fedora
