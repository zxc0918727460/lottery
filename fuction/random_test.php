<?php
	$test_number = 10000;
	$bingo_max = 39;
	$bingo_min = 1;
	$lottery_numbers = array();


	for($i=0;$i<$test_number;$i++){
		$random_star = rand(1,10);
		for($j=0;$j<$random_star;$j++){

			$random_number = rand($bingo_min,$bingo_max);
			if(in_array($random_numbers, $lottery_numbers[$i])){
				$i--;
			}else{
				$lottery_numbers[$i][$j] = $random_number;
			}
		}
	}

	  echo "<script>console.log( '".$lottery_numbers."' );</script>";
?>