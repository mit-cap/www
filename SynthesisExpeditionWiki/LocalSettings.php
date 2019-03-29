<?php

# This file was automatically generated by the MediaWiki installer.
# If you make manual changes, please keep track in case you need to
# recreate them later.
#
# See includes/DefaultSettings.php for all configurable settings
# and their default values, but don't forget to make changes in _this_
# file, not there.
#
# Further documentation for configuration settings may be found at:
# http://www.mediawiki.org/wiki/Manual:Configuration_settings

# If you customize your file layout, set $IP to the directory that contains
# the other MediaWiki files. It will be used as a base to locate files.
if( defined( 'MW_INSTALL_PATH' ) ) {
	$IP = MW_INSTALL_PATH;
} else {
	$IP = dirname( __FILE__ );
}

$path = array( $IP, "$IP/includes", "$IP/languages" );
set_include_path( implode( PATH_SEPARATOR, $path ) . PATH_SEPARATOR . get_include_path() );

require_once( "$IP/includes/DefaultSettings.php" );

# If PHP's memory limit is very low, some operations may fail.
# ini_set( 'memory_limit', '20M' );

if ( $wgCommandLineMode ) {
	if ( isset( $_SERVER ) && array_key_exists( 'REQUEST_METHOD', $_SERVER ) ) {
		die( "This script must be run from the command line\n" );
	}
}
## Uncomment this to disable output compression
# $wgDisableOutputCompression = true;

$wgSitename         = "Synthesis Expedition Proposal";

## The URL base path to the directory containing the wiki;
## defaults for all runtime URL paths are based off of this.
## For more information on customizing the URLs please see:
## http://www.mediawiki.org/wiki/Manual:Short_URL
$wgScriptPath       = "/cap/SynthesisExpeditionWiki";
$wgScriptExtension  = ".php";

## UPO means: this is also a user preference option

$wgEnableEmail      = true;
$wgEnableUserEmail  = true; # UPO

$wgEmergencyContact = "help@csail.mit.edu";
$wgPasswordSender = "help@csail.mit.edu";

$wgEnotifUserTalk = true; # UPO
$wgEnotifWatchlist = true; # UPO
$wgEmailAuthentication = true;

## Database settings
$wgDBtype           = "postgres";
$wgDBserver         = "postgres.csail.mit.edu";
$wgDBname           = "mediawiki";
$wgDBuser           = "wiki/cap";
$wgDBpassword       = "Zqilm<3U2";

# Postgres specific settings
$wgDBport           = "5432";
$wgDBmwschema       = "cap";
$wgDBts2schema      = "public";

## Shared memory settings
$wgMainCacheType = CACHE_NONE;
$wgMemCachedServers = array();

## To enable image uploads, make sure the 'images' directory
## is writable, then set this to true:
$wgEnableUploads       = true;
$wgUseImageMagick = true;
$wgImageMagickConvertCommand = "/usr/bin/convert";

## If you use ImageMagick (or any other shell command) on a
## Linux server, this will need to be set to the name of an
## available UTF-8 locale
# $wgShellLocale = "en_US.UTF-8";

## If you want to use image uploads under safe mode,
## create the directories images/archive, images/thumb and
## images/temp, and make them all writable. Then uncomment
## this, if it's not already uncommented:
# $wgHashedUploadDirectory = false;

## If you have the appropriate support software installed
## you can enable inline LaTeX equations:
$wgUseTeX           = true;

$wgLocalInterwiki   = $wgSitename;

$wgLanguageCode = "en";

$wgProxyKey = "4b5edf713c65d98114835cde71fc32a6b0aa449eb29ae8d3d7b5e88481566608";

## Default skin: you can change the default skin. Use the internal symbolic
## names, ie 'standard', 'nostalgia', 'cologneblue', 'monobook':
$wgDefaultSkin = 'monobook';

## For attaching licensing metadata to pages, and displaying an
## appropriate copyright notice / icon. GNU Free Documentation
## License and Creative Commons licenses are supported so far.
# $wgEnableCreativeCommonsRdf = true;
$wgRightsPage = ""; # Set to the title of a wiki page that describes your license/copyright
$wgRightsUrl = "";
$wgRightsText = "";
$wgRightsIcon = "";
# $wgRightsCode = ""; # Not yet used

# Emit cookies that are specific to this Wiki.
$wgCookieDomain = 'groups.csail.mit.edu';
$wgCookiePath = '/cap/SynthesisExpeditionWiki';

# Send an ETag: header when responding to help caches.
$wgUseETag = true;

# No anonymous users here, so allow crawlers to follow external links.
$wgNoFollowLinks = false;

# We have a system-wide copy of texvc.
$wgTexvc = "/usr/local/csail/bin/texvc";

# Enable the CategoryTree extension and other Ajax functionality
$wgUseAjax = true;
require_once("{$IP}/extensions/CategoryTree/CategoryTree.php");

# Support for automatic footnote numbering
require_once("{$IP}/extensions/Cite/Cite.php");

# Support for special "insert character" JavaScript on edit pages
require_once("{$IP}/extensions/CharInsert/CharInsert.php");

# This snippet prevents new registrations from anonymous users
# (Sysops can still create user accounts)
$wgGroupPermissions['*']['createaccount'] = false;

# This snippet prevents editing from anonymous users
$wgGroupPermissions['*']['edit'] = false;
$wgGroupPermissions['*']['createtalk'] = false;
$wgGroupPermissions['*']['createpage'] = false;
$wgGroupPermissions['*']['writeapi'] = false;

$wgGroupPermissions['*']['read'] = false;

# Pages anonymous (not-logged-in) users may see
$wgWhitelistRead = array( ":Main Page", "Special:Userlogin", "Wikipedia:Help" );
 
# Use SSL certificate authentication
require_once("{$IP}/extensions/SSLAuthPluginConfig.php");

$wgDiff3 = "/usr/bin/diff3";
$wgLogo = "$wgScriptPath/images/caplogo.png";

# When you make changes to this configuration file, this will make
# sure that cached pages are cleared.
$wgCacheEpoch = max( $wgCacheEpoch, gmdate( 'YmdHis', @filemtime( __FILE__ ) ) );