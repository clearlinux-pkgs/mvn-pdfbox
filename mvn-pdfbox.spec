#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-pdfbox
Version  : 2.0.4
Release  : 3
URL      : https://repo1.maven.org/maven2/org/apache/pdfbox/fontbox/2.0.4/fontbox-2.0.4.jar
Source0  : https://repo1.maven.org/maven2/org/apache/pdfbox/fontbox/2.0.4/fontbox-2.0.4.jar
Source1  : https://repo1.maven.org/maven2/org/apache/pdfbox/fontbox/2.0.4/fontbox-2.0.4.pom
Source2  : https://repo1.maven.org/maven2/org/apache/pdfbox/pdfbox-parent/2.0.4/pdfbox-parent-2.0.4.pom
Source3  : https://repo1.maven.org/maven2/org/apache/pdfbox/pdfbox/2.0.3/pdfbox-2.0.3.jar
Source4  : https://repo1.maven.org/maven2/org/apache/pdfbox/pdfbox/2.0.3/pdfbox-2.0.3.pom
Source5  : https://repo1.maven.org/maven2/org/apache/pdfbox/pdfbox/2.0.4/pdfbox-2.0.4.jar
Source6  : https://repo1.maven.org/maven2/org/apache/pdfbox/pdfbox/2.0.4/pdfbox-2.0.4.pom
Source7  : https://repo1.maven.org/maven2/org/apache/pdfbox/pdfbox/2.0.9/pdfbox-2.0.9.jar
Source8  : https://repo1.maven.org/maven2/org/apache/pdfbox/pdfbox/2.0.9/pdfbox-2.0.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-pdfbox-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-pdfbox package.
Group: Data

%description data
data components for the mvn-pdfbox package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/fontbox/2.0.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/fontbox/2.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/fontbox/2.0.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/fontbox/2.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox-parent/2.0.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox-parent/2.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.9
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.9

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.9
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.9


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/pdfbox/fontbox/2.0.4/fontbox-2.0.4.jar
/usr/share/java/.m2/repository/org/apache/pdfbox/fontbox/2.0.4/fontbox-2.0.4.pom
/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox-parent/2.0.4/pdfbox-parent-2.0.4.pom
/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.3/pdfbox-2.0.3.jar
/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.3/pdfbox-2.0.3.pom
/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.4/pdfbox-2.0.4.jar
/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.4/pdfbox-2.0.4.pom
/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.9/pdfbox-2.0.9.jar
/usr/share/java/.m2/repository/org/apache/pdfbox/pdfbox/2.0.9/pdfbox-2.0.9.pom
