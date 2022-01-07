import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-display-options',
  templateUrl: './display-options.component.html',
  styleUrls: ['./display-options.component.css']
})
export class DisplayOptionsComponent implements OnInit {

  constructor() { }

  showView: any;
  one: any;
  two: any;
  three: any;
  four: any;
  five: any;

  ngOnInit(): void {
    this.one = true;
  }

  view(id: number) {
    this.showView = id;
    switch (id) {
      case 1:
        this.one = true;
        this.two = this.three = this.four = this.five = false;
        break;
      case 2:
        this.two = true;
        this.one = this.three = this.four = this.five = false;
        break;
      case 3:
        this.three = true;
        this.one = this.two = this.four = this.five = false;
        break;
      case 4:
        this.four = true;
        this.one = this.two = this.three = this.five = false;
        break;
      case 5:
        this.one = this.two = this.three = this.four = false;
        this.five = true;
        break;
    }
  }
}
