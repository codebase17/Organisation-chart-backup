import { getLocaleDateFormat } from "@angular/common";
import { asNativeElements } from "@angular/core";
import { result, template } from "lodash";
import { OrganisationChartStructure } from "../models/organisation-chart-structure";
import { OrganisationChartService } from "../services/organisation-chart.service";

export class OrganisationChartStructureExtension {

  ans: OrganisationChartStructure[] = [];
  temp: OrganisationChartStructure[] = [];

  constructor(private organisationService:OrganisationChartService) { }

  public parentKeyAbsent(OrganisationChartStructure: OrganisationChartStructure): boolean {
    return (
      OrganisationChartStructure.reportingManagerId === undefined ||
      OrganisationChartStructure.reportingManagerId === null ||
      OrganisationChartStructure.reportingManagerId === 0)
  }

  public searchItem(OrganisationChartStructures: OrganisationChartStructure[], searchId: number): any {
    let foundItem = null;

    for (let index = 0; index < OrganisationChartStructures.length; index++) {
      if (OrganisationChartStructures[index].employeeId === searchId) {
        foundItem = OrganisationChartStructures[index];
        break;
      }

      if (OrganisationChartStructures[index].reportees !== undefined &&
        OrganisationChartStructures[index].reportees.length > 0) {
        foundItem = this.searchItem(OrganisationChartStructures[index].reportees, searchId);
      }

      if (foundItem !== null)
        break;
    }

    return foundItem;
  }

  public getData(fldEmpId):OrganisationChartStructure[]
  {
    let reporteesTemp: OrganisationChartStructure[] = [];
    this.organisationService.getSubEmployee(fldEmpId).subscribe((res:any) => {  
      console.log("sub employees of",fldEmpId,res);
      for(let j=0;j<res.Data.length;j++)
      {
        let emp = new OrganisationChartStructure();
        emp.employeeId = res.Data[j].FLD_EMP_ID;
        emp.employeeName = res.Data[j].FLD_FULL_NAME;
        emp.checked =false;
        emp.reportingManagerId = res.Data[j].FLD_SPONSOR_ID;
        emp.reportees = this.getData(res.Data[j].FLD_EMP_ID);

        console.log("emp",emp);
    
        reporteesTemp.push(emp);
      }
    });
    return reporteesTemp;
  }

  public generateData(): OrganisationChartStructure[] {

    this.organisationService.getEmployee(1).subscribe((res:any) => {
      console.log("extension",res.Data);
      
      for(let i=0;i<res.Data.length;i++)
      {
          console.log("dataaaaa",res.Data[i]);
          let emp = new OrganisationChartStructure();
          emp.employeeId = res.Data[i].FLD_EMP_ID;
          emp.employeeName = res.Data[i].FLD_FULL_NAME;
          emp.checked =false;
          emp.reportingManagerId = res.Data[i].FLD_SPONSOR_ID;
          emp.reportees = [];

          let temp = this.getData(res.Data[i].FLD_EMP_ID);
          console.log(temp);
          emp.reportees = temp;
          this.ans.push(emp);
      }

    });

    return this.ans;

  }

}