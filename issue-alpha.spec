Summary:	PLD Linux release file with virtual keyboard
Summary(pl):	Wersja Linuksa PLD z wirtualn± klawiatur±
Name:		issue-alpha
Version:	1.0
Release:	1
License:	GPL
Group:		Base
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
Obsoletes:	issue
Obsoletes:	issue-fancy
Obsoletes:	issue-logo
Obsoletes:	issue-pure
Obsoletes:	redhat-release
Obsoletes:	mandrake-release

%description
PLD Linux release file with virtual keyboard. Can be used to some
hacks with gpm on systems w/o available keyboard or as paranoic
security login solution (anti keyloggers).

%description -l pl
Wersja Linuksa PLD z wirtualn± klawiatur±. Mo¿e byæ u¿yta do manewrów
za pomoc± gpma w systemach bez sprawnej klawiatury, b±d¼ jako poprawa
bezpieczeñstwa logowania dla paranoików (przeciwdzia³a keyloggerom).

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
.-------------< PLD Linux 1.0 (Ra) >--------------.
|                                                 |
|  ~  !  "  #  $  %  ^  &  *  (  )  _  +          |
| ´ \`  1  2  3  4  5  6  7  8  9  0  -  =         |
|                                                :'
|                                {  }            ;
|  Qq Ww Ee Rr Tt Yy Uu Ii Oo Pp  [  ]          ;
|                               :  @  ~       .;
|    Aa Ss Dd Ff Gg Hh Jj Kk Ll  ;  '  #     :;
:   |                       <  >  ?        .;'
\`:   \\\\ Zz Xx Cc Vv Bb Nn Mm  ,  .  /   ,.;'"
  \`..                           ,..;:'"
     \`-------------------------´

EOF

cat $RPM_BUILD_ROOT%{_sysconfdir}/issue.net > $RPM_BUILD_ROOT%{_sysconfdir}/issue
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
