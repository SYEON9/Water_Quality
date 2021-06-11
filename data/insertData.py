db.local.insertMany([
{
	name: "경상북도",
	purification_plant: [
		{purification:"부남정수장", date:"20190618", taste:"적합", smell:"적합", color: 1, pH:7.47 ,NTU:0.040 ,residual_chlorine: 0.82}, 
		{purification:"부남정수장", date:"20190617", taste:"적합", smell:"적합", color: 0, pH:7.42 ,NTU:0.020 ,residual_chlorine: 0.89}, 
		{purification:"부남정수장", date:"20190616", taste:"적합", smell:"적합", color: 0, pH:7.47 ,NTU:0.020 ,residual_chlorine: 0.79},
		{purification:"안덕정수장", date:"20190618", taste:"적합", smell:"적합", color: 1, pH:7.43 ,NTU:0.100 ,residual_chlorine: 1.23},
		{purification:"안덕정수장", date:"20190617", taste:"적합", smell:"적합", color: 1, pH:7.44 ,NTU:0.120 ,residual_chlorine: 1.10},
		{purification:"안덕정수장", date:"20190616", taste:"적합", smell:"적합", color: 1, pH:7.45 ,NTU:0.160 ,residual_chlorine: 1.09},
		{purification:"주왕산정수장", date:"20190618", taste:"적합", smell:"적합", color: 1, pH:7.44 ,NTU:0.070 ,residual_chlorine: 0.56},
		{purification:"주왕산정수장", date:"20190617", taste:"적합", smell:"적합", color: 1, pH:7.41 ,NTU:0.090 ,residual_chlorine: 0.69},
		{purification:"주왕산정수장", date:"20190616", taste:"적합", smell:"적합", color: 0, pH:7.49 ,NTU:0.140 ,residual_chlorine: 0.72}
		
	],
	multiPurpose_dam: [
		{dam:"안동댐", month:"06", pH: 7.0, DO: 10.6, BOD:1.0 ,COD:2.8 ,NTU:0.9 }, 
		{dam:"안동댐", month:"05", pH: 7.5, DO: 9.6, BOD:1.3 ,COD:2.8 ,NTU:0.3},
		{dam:"안동댐", month:"04", pH: 7.4, DO: 11.0, BOD:1.0 ,COD:2.4 ,NTU:1.6}
	]
},
{
name: "경상남도",
	purification_plant: [
		{purification:"일운정수장", date:"20190618", taste:"적합", smell:"적합", color: 0, pH:7.11 ,NTU:0.057 ,residual_chlorine: 0.66}, 
		{purification:"일운정수장", date:"20190617", taste:"적합", smell:"적합", color: 0, pH:7.11 ,NTU:0.066 ,residual_chlorine: 0.72}, 
		{purification:"일운정수장", date:"20190616", taste:"적합", smell:"적합", color: 0, pH:7.11 ,NTU:0.069 ,residual_chlorine: 0.71}
	],
	multiPurpose_dam: [
		{dam:"밀양댐", month:"06", pH: 7.2, DO: 9.5, BOD:0.7 ,COD:0.8 ,NTU:2.8 }, 
		{dam:"밀양댐", month:"05", pH: 7.0, DO: 9.7, BOD:0.8 ,COD:1.3 ,NTU:3.1},
		{dam:"밀양댐", month:"04", pH: 7.1, DO: 10.7, BOD:0.7 ,COD:1.9 ,NTU:1.1},
		{dam:"남강댐", month:"06", pH: 7.7, DO: 8.5, BOD:0.3 ,COD:4.1 ,NTU:2.3 }, 
		{dam:"남강댐", month:"05", pH: 7.7, DO: 10.3, BOD:1.6 ,COD:3.0 ,NTU:15.8},
		{dam:"남강댐", month:"04", pH: 8.1, DO: 9.8, BOD:1.4 ,COD:5.3 ,NTU:1.3},
		{dam:"합천댐", month:"06", pH: 9.7, DO: 9.5, BOD:0.7 ,COD:0.8 ,NTU:1.1 }, 
		{dam:"합천댐", month:"05", pH: 7.4, DO: 10.6, BOD:0.7 ,COD:1.5 ,NTU:1.0},
		{dam:"합천댐", month:"04", pH: 8.0, DO: 10.3, BOD:0.6 ,COD:2.3 ,NTU:0.5}	
	]
}
])

