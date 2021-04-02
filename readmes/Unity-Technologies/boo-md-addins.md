# Building #

git clone git://github.com/bamboo/boo

git clone git://github.com/bamboo/boo-extensions

git clone git://github.com/bamboo/boo-md-addins

cd boo-md-addins

cat > build.properties

	<project name="build properties">
		<property name="md.bin.dir" value="/usr/lib/monodevelop/bin" />
		<property name="nunit.framework.dll" value="/usr/lib/cli/nunit.framework-2.4/nunit.framework.dll" />
	</project>
	
nant


