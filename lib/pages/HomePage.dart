import 'package:flutter/material.dart';
import 'package:percent_indicator/percent_indicator.dart';
import 'package:sixmar/values/app_assets.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(children: [
        Expanded(child: Image.asset(AppAssets.iSaveMoney)),
        Expanded(
            child: new LinearPercentIndicator(
          width: 170.0,
          animation: true,
          animationDuration: 1000,
          lineHeight: 20.0,
          leading: new Text("left content"),
          trailing: new Text("right content"),
          percent: 0.2,
          center: Text("20.0%"),
          linearStrokeCap: LinearStrokeCap.butt,
          progressColor: AppColors.appBar,
        ))
      ]),
    );
  }
}
