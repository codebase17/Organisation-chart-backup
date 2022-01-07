import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { DisplayEmployeeDetailsComponent } from '../display-employee-details/display-employee-details.component';

@Injectable({
  providedIn: 'root'
})
export class OrganisationChartService {

  readonly APIUrl = "http://127.0.0.1:8000";

  constructor(private http:HttpClient) { }

  private employeeIdSource = new BehaviorSubject(0);
  employeeIdValue = this.employeeIdSource.value;

  setEmployeeId(val:number){
    this.employeeIdValue = val;
  }

  getEmployeeId(){
    return this.employeeIdValue;
  }

  getAllEmployees(){
    return this.http.get(this.APIUrl + '/services/hrms/organisation_chart');
  }

  getEmployee(val:any){
    return this.http.get(this.APIUrl + '/services/hrms/get_employee?q=' + val);
  }

  getSubEmployee(val:any){
    return this.http.get(this.APIUrl + '/services/hrms/get_sub_employee?q=' + val);
  }



}
