# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       xorg-x11-proto-videoproto
Summary:    X.Org X11 Protocol videoproto
Version:    2.3.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/videoproto-%{version}.tar.bz2
Source100:  xorg-x11-proto-videoproto.yaml
Provides:   videoproto


%description
This extension provides a protocol for a video output mechanism,
mainly to rescale video playback in the video controller hardware.




%prep
%setup -q -n videoproto-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post






%files
%defattr(-,root,root,-)
# >> files
%{_datadir}/pkgconfig/videoproto.pc
%{_includedir}/X11/extensions/vldXvMC.h
%{_includedir}/X11/extensions/Xvproto.h
%{_includedir}/X11/extensions/Xv.h
%{_includedir}/X11/extensions/XvMC.h
%{_includedir}/X11/extensions/XvMCproto.h
%doc %{_docdir}/videoproto/xv-protocol-v2.txt
# << files


