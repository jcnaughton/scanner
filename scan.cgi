#!/usr/bin/perl

    use CGI;
    my $q = CGI->new;
	
    $name  = $q->param('name');
    $res  = $q->param('res');
    $mode  = $q->param('mode');

	
    if ($name eq '') {
     $name=`date +%s`; chomp $name;
    }
    $jpg="\/scans\/" . $name . ".jpg";
    $pdf="\/scans\/" . $name . ".pdf";
	
	
    print $q->header();

    print "<html><body><p>Starting scan......</p>\n";
    @scanimage=`scanimage -d 'hpaio:/usb/Deskjet_3050_J610_series?serial=CN115394RT05HX' --mode\=$mode --format\=jpeg --resolution\=$res > $jpg`;

    @chmod=`chmod 777 $jpg`;

    @convert=`convert $jpg $pdf`;

    print "<p>Scan complete $jpg</p>";

    print "<a href='index.html'>scan another</a>\n";

    print "<table border\=\'1\'>\n";

    print "<tr><th>jpg</th><th>pdf</th></tr>\n"; 

    print "<tr><td><a href\=\'$jpg\' target\=\'new_window\'><img src\=\'$jpg\' width\=\'400\' ></a></td>\n";

    print "<td><a href\=\'$pdf\'target\=\'new_window\'>$pdf</a></td></tr>\n";

    print "</body></html>";
