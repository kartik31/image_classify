<?php
function foo($x)
{
$data = "/var/www/html/./$x.png";
$data_string = $data;
$ch = curl_init('http://35.184.99.106:5000/');
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json','Content-Length: ' . strlen($data_string))
);
$result = curl_exec($ch);
//echo $result;
return $result ;

}
?>
