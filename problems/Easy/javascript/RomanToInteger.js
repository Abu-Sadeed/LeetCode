//! Initial 222ms and 48.3mb 

// var romanToInt = function (s) {
// 	let total = 0;
// 	var letterToNum = {
// 		'I': 1,
// 		'V': 5,
// 		'X': 10,
// 		'L': 50,
// 		'C': 100,
// 		'D': 500,
// 		'M': 1000
// 	}
// 	for (let i = 0; i < s.length; i++) {
// 		val = s[i]
// 		if (val === 'I' && (s[i + 1] === 'V' || s[i + 1] === 'X')) {
// 			total = total - letterToNum[val]
// 		} else if (val === 'X' && (s[i + 1] === 'L' || s[i + 1] === 'C')) {
// 			total = total - letterToNum[val]
// 		} else if (val === 'C' && (s[i + 1] === 'D' || s[i + 1] === 'M')) {
// 			total = total - letterToNum[val]
// 		} else {
// 			total = total + letterToNum[val]
// 		}

// 	}
// 	return total;
// };


//! Idea from discussion worse than mine 311ms 50.6mb 

var romanToInt = function (s) {
	let total = 0;
	var letterToNum = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}

	var reduceNumber = {
		'IV': 4,
		'IX': 9,
		'XL': 40,
		'XC': 90,
		'CD': 400,
		'CM': 900
	}

	const keys = Object.keys(reduceNumber)

	for (let i = 0; i < keys.length; i++) {
		if (s.includes(keys[i])) {
			total = total + reduceNumber[keys[i]];
			console.log(total)
			s = s.replace(keys[i], "");
		}

	}

	for (let i = 0; i < s.length; i++) {
		val = s[i]

		total = total + letterToNum[val]


	}

	return total;
};