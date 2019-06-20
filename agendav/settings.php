<?php

// Site title
$app['site.title'] = 'Noisebridge Calendar';

// Site logo (should be placed in public/img). Optional
$app['site.logo'] = 'nb.logo.png';

// Site footer. Optional
$app['site.footer'] = 'Be Excellent';

// Trusted proxy ips
$app['proxies'] = [];

// Database settings
$app['db.options'] = [
        'dbname' => 'agendav',
        'user' => 'noisebridge',
        'password' => 'noisebridge',
        'host' => 'postgres',
        'driver' => 'pdo_pgsql'
];

// Encryption key
$app['encryption.key'] = '';

// Log path
$app['log.path'] = '/tmp/';

// Base URL
$app['caldav.baseurl'] = 'http://radicale:5232/noisebridge';

// Authentication method required by CalDAV server (basic or digest)
$app['caldav.authmethod'] = 'basic';

// Whether to show public CalDAV urls
$app['caldav.publicurls'] = true;

// Whether to show public CalDAV urls
$app['caldav.baseurl.public'] = 'http://localhost:5232';

// Default timezone
$app['defaults.timezone'] = 'America/Los_Angeles';

// Default languajge
$app['defaults.language'] = '';

// Default time format. Options: '12' / '24'
$app['defaults.time.format'] = '24';

/*
 * Default date format. Options:
 *
 * - ymd: YYYY-mm-dd
 * - dmy: dd-mm-YYYY
 * - mdy: mm-dd-YYYY
 */
$app['defaults.date.format'] = 'ymd';

// Default first day of week. Options: 0 (Sunday), 1 (Monday)
$app['defaults.weekstart'] = 0;

// Logout redirection. Optional
$app['logout.redirection'] = '';

// Calendar sharing
$app['calendar.sharing'] = false;
