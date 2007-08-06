
%define	distname	Th
%define	distversion	2.99
%define	distrelease	"%{distversion} PLD Linux (%{distname})"

Summary:	PLD Linux release file with virtual keyboard
Summary(pl.UTF-8):	Wersja Linuksa PLD z wirtualną klawiaturą
Name:		issue-alpha
Version:	%{distversion}
Release:	2
License:	GPL
Group:		Base
Provides:	issue
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file with virtual keyboard. Can be used to some
hacks with gpm on systems w/o available keyboard or as paranoic
security login solution (anti keyloggers).

%description -l pl.UTF-8
Wersja Linuksa PLD z wirtualną klawiaturą. Może być użyta do manewrów
za pomocą gpma w systemach bez sprawnej klawiatury, bądź jako poprawa
bezpieczeństwa logowania dla paranoików (przeciwdziała keyloggerom).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
.-------------< PLD Linux %{distversion} (%{distname}) >--------------.
|                                                 |
|  ~  !  "  #  $  %  ^  &  *  (  )  _  +          |
| ' \`  1  2  3  4  5  6  7  8  9  0  -  =         |
|                                                :'
|                                {  }            ;
|  Qq Ww Ee Rr Tt Yy Uu Ii Oo Pp  [  ]          ;
|                               :  @  ~       .;
|    Aa Ss Dd Ff Gg Hh Jj Kk Ll  ;  '  #     :;
:   |                       <  >  ?        .;'
\`:   \\\\ Zz Xx Cc Vv Bb Nn Mm  ,  .  /   ,.;'"
  \`..                           ,..;:'"
     \`-------------------------'

EOF

cat $RPM_BUILD_ROOT%{_sysconfdir}/issue.net > $RPM_BUILD_ROOT%{_sysconfdir}/issue
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

echo %{distrelease} > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
