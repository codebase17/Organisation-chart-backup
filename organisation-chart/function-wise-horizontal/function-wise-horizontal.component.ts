import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-function-wise-horizontal',
  templateUrl: './function-wise-horizontal.component.html',
  styleUrls: ['./function-wise-horizontal.component.css']
})
export class FunctionWiseHorizontalComponent implements OnInit {

  constructor() { }

  count: any = [1,2,3,4,5,6,7,8,9,10];

  ngOnInit(): void {
    console.log(this.count);
  }

}
