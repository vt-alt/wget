# -*- rpm-spec -*-
# $Id: wget,v 1.1 2004/03/19 10:48:41 grigory Exp $

%define beta %nil

Name: wget
Version: 1.12
Release: alt1
#Release: alt0.%beta

Summary: An utility for retrieving files using the HTTP, HTTPS or FTP protocols
License: GPLv3
Group: Networking/WWW

Url: http://www.gnu.org/software/wget/wget.html
Source: ftp://ftp.gnu.org/gnu/wget/%name-%version.tar.bz2
#Source: ftp://ftp.gnu.org/gnu/wget/%name-%version-%beta.tar.gz
Patch1: %name-1.9.1-alt-texinfo.patch
Patch2: %name-1.6-mdk-passive_ftp.patch
Patch3: %name-1.7-alt-locale.patch
#Patch4: %name-1.8.1-alt-quiet.patch
Patch10: wget-1.10.1-alt-ntlm-buffer.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Jun 29 2005
BuildRequires: gcc-c++ hostinfo libssl-devel libstdc++-devel


Summary(es):	Cliente en l�nea de comando para bajar archivos WWW/FTP con recursi�n opcional
Summary(fr):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl):	Wsadowy klient HTTP/FTP
Summary(pt_BR):	Cliente na linha de comando para baixar arquivos WWW/FTP com recurs�o opcional
Summary(ru_RU.KOI8-R):	������� ��� ��������� ������ �� ���������� HTTP � FTP
Summary(uk_UA.KOI8-U):	���̦�� ��� ��������� ���̦� �� ���������� HTTP �� FTP
Summary(zh_CN):	[ͨѶ]����ǿ������س���,֧�ֶϵ�����

%description
GNU Wget is a file retrieval utility which can use either the HTTP,
HTTPS or FTP protocols.  Wget features include the ability to work
in the background while you're logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

Install wget if you need to retrieve large numbers of files with HTTP,
HTTPS or FTP, or if you need a utility for mirroring web sites or FTP
directories.

%description -l es
GNU wget es una herramienta de red para bajar archivos usando HTTP y
FTP. Funciona en modo no interactivo, pudiendo trabajar en background.
Funciona muy bien, incluso en conexiones lentas o inestables, bajando
el archivo hasta que sea completamente recibido.

%description -l fr
GNU Wget est un utilitaire pour r�cup�rer des fichiers qui peut
utiliser indiff�remment les protocoles HTTP ou FTP. Parmi les
caract�ristiques de Wget, citons la capacit� � r�cup�rer des fichiers
en arri�re-plan alors que vous n'�tes pas connect�, la r�cup�ration
r�cursive de r�pertoires, la capacit� de r�cup�rer des fichiers en
appliquant un filtre sur le nom ou sur la date, la gestion de Rest
avec les serveurs FTP et de Range avec les serveurs HTTP pour
r�cup�rer des fichiers avec une connexion lente ou instable, le
support des serveurs Proxy... Wget est particuli�rement configurable.

%description -l ja
GNU wget �� HTTP �� FTP �ץ�ȥ���Τɤ��餫����Ѥ��뤳�Ȥ��Ǥ���
�ե�������������桼�ƥ���ƥ��Ǥ���wget �ϥ������Ȥ��Ƥ���
�֤˥Хå����饦��ɤ�Ư����ħ���äƤ��뤳�ȡ��ǥ��쥯�ȥ�κƵ�Ū
�������ե�����͡���Υ磻��ɥ����ɥޥå��󥰡��ե�����Υ����ॹ����פ�
��¸����ӡ��٤��԰������³�� FTP �����Ф� Rest �� HTTP �����Ф�
Range �λ��ѡ��ץ����������ФΥ��ݡ��Ȥ�������ưפ���ޤ����ħ��
��äƤ��ޤ���

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do �ci�gania zasob�w
wsadowo. Umo�liwia �ci�ganie zasob�w z podkatalogami, a tak�e ma opcje
umo�liwiaj�ce wykonanie lokalnej kopii zasob�w (mirror). W razie
niemo�no�ci dostania si� do zasob�w lub gdy po��czenie z serwerem
FTP/HTTP zostanie zerwane, mo�e automatycznie ponawia� pr�by
kopiowania. Jest tak�e dobrze przystosowany do tego, �eby uruchamia�
go jako zadanie z crona.

%description -l pt_BR
O GNU wget � uma ferramenta de rede para baixar arquivos usando HTTP e
FTP. Ele funciona em modo n�o interativo, podendo trabalhar em
background. Funciona muito bem, mesmo em conex�es lentas ou inst�veis,
baixando o arquivo at� que ele seja completamente recebido.

%description -l ru_RU.KOI8-R
GNU Wget - ��� ������� ��������� ������ ��� ��������� ������ ��
���������� FTP � HTTP. ����� ������������ Wget - ������ � �������
������ ����� ������ �� �������, ����������� ���������� ���������,
����� ������ �� �������, ��������� ������� ��������� � ���������
������, ���������� ������� ��������� ������ ��� ��������,
������������� REST � FTP ��������� � Range � HTTP ��������� ���
�������� ������ �� ��������� ��� ������������ �������, ��������� 
������-��������, �����������������.

%description -l uk_UA.KOI8-U
GNU Wget - �� ���̦�� ���������� ����� ��� ��������� ���̦� ��
���������� FTP �� HTTP. ����� ����������� Wget - ������ � ��������
����ͦ Ц��� ������ �� �������, ���������� ��������� ������Ǧ�,
��¦� ���̦� �� �������, ��Ҧ������ ���� צ�������� �� ���������
���̦�, ���������� ���� צ�������� ���̦� ��� ����������Φ,
������������ REST � FTP ��������� �� Range � HTTP ��������� ���
������������ ���̦� �� ��צ����� �� �����¦����� �������, Ц�������
����Ӧ-�����Ҧ�, �����������Φ���.

%prep
%setup -q -n %name-%version
#setup -q -n %name-%version-%beta

# Fix docs and samples.
rm -f doc/*.info*
find doc -type f -print0 |
	xargs -r0 grep -FZl /usr/local/ -- |
	xargs -r0 sed -i 's,/usr/local/,/,g' --

%patch1 -p1
#patch2 -p1
#patch3 -p1
#%patch4 -p1
%patch10 -p1

%build
%configure --with-ssl
# https://bugzilla.altlinux.org/show_bug.cgi?id=14239
(cd po; make update-po)
%make_build

%install
%makeinstall

%find_lang %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/%{name}rc
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc AUTHORS MAILING-LIST NEWS README*

%changelog
* Wed Sep 23 2009 Michael Shigorin <mike@altlinux.org> 1.12-alt1
- 1.12
  + fixes security problem outlined in RH#520454:
    SSL certificate name vs. host name verification bypass
    via NUL ('\0') character embedded in X509 certificate's
    CommonName or subjectAltName
  + thanks ldv@ for heads-up

* Sun Jul 26 2009 Michael Shigorin <mike@altlinux.org> 1.11.4-alt2
- applied repocop patch

* Fri Oct 31 2008 Michael Shigorin <mike@altlinux.org> 1.11.4-alt1
- 1.11.4 (1.11.2 should have fixed #17676)

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.11.1-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Mar 28 2008 Michael Shigorin <mike@altlinux.org> 1.11.1-alt1
- 1.11.1

* Mon Feb 11 2008 Michael Shigorin <mike@altlinux.org> 1.11.1-alt0.b2092
- 1.1.11-b2092

* Wed Jan 30 2008 Michael Shigorin <mike@altlinux.org> 1.11-alt2
- added workaround for #14239 (crash in ru_RU.UTF-8 while
  all OK in C, ru_RU.KOI8-R, uk_UA.UTF-8); that is, removed
  translations till 1.11.1: https://savannah.gnu.org/bugs/?22161

* Sun Jan 27 2008 Michael Shigorin <mike@altlinux.org> 1.11-alt1
- 1.11
  + License: changed to GPLv3
  + see announce here:
    http://www.mail-archive.com/wget%%40sunsite.dk/msg10768.html

* Thu Nov 01 2007 Michael Shigorin <mike@altlinux.org> 1.10.2-alt3
- fixed #13241, thanks inger@

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 1.10.2-alt2
- added ru/uk package description charsets (#11848)
- spec macro abuse cleanup

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.10.2-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Oct 15 2005 Michael Shigorin <mike@altlinux.org> 1.10.2-alt1
- 1.10.2
- security fix for CAN-2005-3185 (NTLM buffer overflow)
  provided by upstream vendor
- disabled patch2

* Thu Oct 13 2005 Michael Shigorin <mike@altlinux.org> 1.10.1-alt2
- security fix: NTLM buffer overflow
  + patch by Sergey Ryabchun (sr@)
  + thanks to Dmitry V.Levin (ldv@) for alerting

* Mon Aug 29 2005 Michael Shigorin <mike@altlinux.org> 1.10.1-alt1
- 1.10.1 (#7789, #7512)
- removed patch3 (merged upstream with minor changes)

* Wed Jun 29 2005 Michael Shigorin <mike@altlinux.org> 1.10-alt1
- 1.10 (thanks Grigory Fateyev <greg anastasia.ru> for testing)
- merged description translations from PLD's 1.9.1-19 spec
- updated buildrequires

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.9.1-alt1.1
- Rebuilt with openssl-0.9.7d.

* Fri Mar 19 2004 Grigory Milev <week@altlinux.ru> 1.9.1-alt1
- new version released
- remove unneeded putches due changes in release

* Wed Aug 06 2003 Alexey Voinov <voins@altlinux.ru> 1.8.2-alt4
- updated rh-filename patch.
- fixup wrong fix for directory traversal bug
- fixed buffer overflow (rh-segv patch)

* Wed Dec 11 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.2-alt3
- Merged RH patches:
  * Sat Oct 05 2002 Karsten Hopp <karsten@redhat.de> 1.8.2-5
  - fix directory traversal bug
  * Thu Jul 25 2002 Trond Eivind Glomsr�d <teg@redhat.com> 1.8.2-3
  - Don't segfault when downloading URLs A-B-A (A-A-B worked) #49859

* Fri Nov 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1.8.2-alt2
- rebuild

* Thu Jun 06 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.2-alt1
- 1.8.2
- Fixed .netrc quotation parsing (mdk).

* Tue Feb 05 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.8.1-alt1
- 1.8.1

* Tue Dec 18 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.8-alt1
- 1.8

* Tue Nov 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.7.1-alt1
- 1.7.1

* Mon Oct 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.7-alt2
- Shutup output to screen when using quiet with batch mode (rh).

* Fri Jun 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.7-alt1
- 1.7
- Merged some MDK and RH paches.
- Resurrected manpage.

* Fri Apr 06 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.6-alt2
- New version 1.6
- Fixed texinfo.patch
- Fixed encdec.patch
- Fixed i18n

* Sat Dec 09 2000 Dmitry V. Levin <ldv@fandra.org> 1.5.3gold-ipl2
- Fixed texinfo documentation.
- Fix bug: the characters ";/?=&+" must retain their encoded/decodedstatus.
  (from Anon Sricharoenchai <ans@beethoven.cpe.ku.ac.th>)

* Fri Jun 30 2000 Dmitry V. Levin <ldv@fandra.org> 1.5.3gold-ipl1
- RE and Fandra adaptions.

* Mon Jun 26 2000 Soenke J. Peters <soenke+rpm@simprovement.com>
- included some stuff from CVS tree
- HTTPS support

* Thu Aug 26 1999 Jeff Johnson <jbj@redhat.com>
- don't permit chmod 777 on symlinks (#4725).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0 tree
- add Provides

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 1.5.3

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.5.2

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- modified group to Applications/Networking

* Wed Apr 22 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5.0
- they removed the man page from the distribution (Duh!) and I added it back
  from 1.4.5. Hey, removing the man page is DUMB!

* Fri Nov 14 1997 Cristian Gafton <gafton@redhat.com>
- first build against glibc


