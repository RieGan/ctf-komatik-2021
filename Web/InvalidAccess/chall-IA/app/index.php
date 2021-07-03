<p>
    Only localhost can access
    <!-- s3cr3t_ag3nt -->
</p>
<?php
include "flag.php";
if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    $ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
} else {
    $ip = $_SERVER['REMOTE_ADDR'];
}

echo "Ip            : $ip";
echo "<br>";
echo "User Agent    : $_SERVER[HTTP_USER_AGENT]";
echo "<br>";

if ($ip == "127.0.0.1" && $_SERVER['HTTP_USER_AGENT'] == "s3cr3t_ag3nt") {
    echo $FLAG;
}
