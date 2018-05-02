<?php
	$data = array();
	$data[0]= array(
		 "periods"=>"107016037", "numbers"=> "09,10,16,19,30,31,32,40,42,46,47,49,54,66,67,68,72,73,75","super_number"=>"80","big_or_small"=>"-","single_or_double"=>"小雙"
		);
	$data[1]= array(
		 "periods"=>"107016036", "numbers"=> "16,26,32,33,34,35,36,37,38,55,58,60,61,62,63,64,65,73,74","super_number"=>"77","big_or_small"=>"-","single_or_double"=>"小雙"
		);
	echo json_encode($data);
?>