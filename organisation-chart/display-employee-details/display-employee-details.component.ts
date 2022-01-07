import { Component, OnInit } from '@angular/core';
import { OrganisationChartService } from '../services/organisation-chart.service';

@Component({
  selector: 'app-display-employee-details',
  templateUrl: './display-employee-details.component.html',
  styleUrls: ['./display-employee-details.component.css']
})
export class DisplayEmployeeDetailsComponent implements OnInit {

  constructor(private organisationService:OrganisationChartService) {}
  
  headings: any = ["Employee Name",
  "Employee ID",
  "Employee Type",
  "Gender",
  "Location",
  "Function",
  "Head of Function",
  "Department",
  "Designation",
  "Phone",
  "Mobile",
  "E-mail",
  "Reporting Manager"];
employee: any = ["Shivani",
  "52875",
  "Permanent",
  "Female",
  "Block III",
  "Corporate Information",
  "Amrish Kumar J",
  "CIS/IS/Engineering",
  "Trainee - Software Engineering",
  "+91 8987981712",
  "7090508517",
  "shivani.s@tally.com",
  "Manju Chandran"];

  basicDetails = this.headings.map((v: any, i: string | number) => [v, this.employee[i]]);

  ngOnInit(): void {
    
  }

  displayDetails()
  {
    console.log("Heyyyyy");
  }
  
}
