Summary:	Screen recording of wlroots-based compositors
Name:		wf-recorder
Version:	0.6.0
Release:	2
License:	MIT
Group:		Applications
Source0:	https://github.com/ammen99/wf-recorder/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	23b7dc5037486ab6d2675d9ef338faf3
URL:		https://github.com/ammen99/wf-recorder
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libdrm-devel
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 1.0.5
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	wayland-devel >= 1.20
BuildRequires:	wayland-protocols >= 1.14
Requires:	pipewire-libs >= 1.0.5
Requires:	wayland >= 1.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wf-recorder is a utility program for screen recording of wlroots-based
compositors (more specifically, those that support wlr-screencopy-v1
and xdg-output).

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{fish_compdir}

%meson_install

%{__mv} $RPM_BUILD_ROOT%{_prefix}/share/fish/fish/vendor_completions.d/wf-recorder.fish $RPM_BUILD_ROOT%{fish_compdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/wf-recorder
%{_mandir}/man1/wf-recorder.1*
%{fish_compdir}/wf-recorder.fish
