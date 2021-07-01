<form action="index.php">
    <input type="text" name="echo_me" id="echo" size="80">
    <input type="submit" value="Echo">
    <!-- flag.php -->
</form>
<h3>
    <?php $echo_me = $_GET['echo_me'];
    $cmd = "bash -c 'echo " . $echo_me . "'";
    if (isset($echo_me)) {
        if ($echo_me == "") {
            echo "Don't say it honey!";
        } elseif (preg_match('/[#!@,{}|":>%^&*()$_+=\-\[\]\';?~\\\\]/', $echo_me)) {
            echo "Hekel hush!!";
        } elseif (strpos($echo_me, "cat") !== false) {
            echo "nope!!";
        } elseif (strlen($echo_me) > 15) {
            echo "Too long :(";
        } else {
            echo $cmd;
            echo system($cmd);
        }
    } else {
        highlight_file(__FILE__);
    } ?>