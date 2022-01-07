import { Component, OnInit } from '@angular/core';
import { OrganisationChartService } from '../services/organisation-chart.service';
import { OrganisationChartStructureExtension } from '../organisation-chart-algorithm/organisation-chart-structure-extension';
import { OrganisationChartStructure } from "../models/organisation-chart-structure";
import * as _ from 'lodash';
import { DisplayEmployeeDetailsComponent } from '../display-employee-details/display-employee-details.component';

@Component({
  selector: 'app-employee-wise',
  templateUrl: './employee-wise.component.html',
  styleUrls: ['./employee-wise.component.css']
})
export class EmployeeWiseComponent implements OnInit {

  constructor(private organisationService:OrganisationChartService) { }

  employees: any = [];
  plus:boolean = false;
  minus:boolean = true;
  temp:any;
 
  expandedIndex:number;

  employeesList:any[]=[];

  public OrganisationChartStructureExtension: OrganisationChartStructureExtension = new OrganisationChartStructureExtension(this.organisationService);
  
  public currentItem!: OrganisationChartStructure;

  public selectedItems: OrganisationChartStructure[] = [];

  public allData!: OrganisationChartStructure[];

  public showData!: OrganisationChartStructure[];

  ngOnInit(): void {
    this.allData =
      this.showData = this.OrganisationChartStructureExtension.generateData();
    console.log("show data",this.showData);
  }

  public back() {
    if (this.OrganisationChartStructureExtension.parentKeyAbsent(this.currentItem)) {
      this.showData = this.allData;
      this.currentItem;
      return;
    }

    let foundItem = this.OrganisationChartStructureExtension.searchItem(this.allData, this.currentItem.employeeId);

    this.showData = foundItem.reportees;
    this.currentItem = foundItem;
  }

  public showReportees(treeItem: OrganisationChartStructure,) {
    this.currentItem = treeItem;
    this.showData = treeItem.reportees;
  }

  public changeStatus(treeItem: OrganisationChartStructure, event: any) {
    if (treeItem.checked === undefined ||
      treeItem.checked === null) {
        treeItem.checked = true;
    }
    else {
      treeItem.checked = !treeItem.checked;
    }


    if(treeItem.checked === true){
      this.selectedItems.push(treeItem);
    }
    else {
      _.remove(this.selectedItems, { employeeId: treeItem.employeeId });
    }
  }

  showDetails(val:number){
    //console.log(val);
    this.organisationService.setEmployeeId(val);
  }

}




