import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OrganisationMainComponent } from './organisation-main/organisation-main.component';
import { DisplayOptionsComponent } from './display-options/display-options.component';
import { EmployeeWiseComponent } from './employee-wise/employee-wise.component';
import { FunctionDepartmentWiseVerticalComponent } from './function-department-wise-vertical/function-department-wise-vertical.component';
import { FunctionEmployeeWiseVerticalComponent } from './function-employee-wise-vertical/function-employee-wise-vertical.component';
import { FunctionWiseHorizontalComponent } from './function-wise-horizontal/function-wise-horizontal.component';
import { HeaderComponent } from './header/header.component';
import { LocationWiseComponent } from './location-wise/location-wise.component';
import { SharedModule } from '../shared.module';
import { RouterModule, Routes } from '@angular/router';
import { DisplayEmployeeDetailsComponent } from './display-employee-details/display-employee-details.component';
import { OrganisationChartService } from './services/organisation-chart.service';


const routes: Routes = [
  { path: 'functionDepartmentWiseVertical', component: FunctionDepartmentWiseVerticalComponent },
  { path: 'functionEmployeeWiseVertical', component: FunctionEmployeeWiseVerticalComponent },
  { path: 'functionWiseHorizontal', component: FunctionWiseHorizontalComponent },
  { path: 'locationWise', component: LocationWiseComponent },
  { path: 'employeeWise', component: EmployeeWiseComponent },
  { path: 'displayOptions', component: DisplayOptionsComponent },
  { path: 'header', component: HeaderComponent },
  { path: 'displayEmployeeDetails', component: DisplayEmployeeDetailsComponent },
  { path: '', component: OrganisationMainComponent },
  ]
  

@NgModule({
  declarations: [OrganisationMainComponent, DisplayOptionsComponent, EmployeeWiseComponent, FunctionDepartmentWiseVerticalComponent, FunctionEmployeeWiseVerticalComponent, FunctionWiseHorizontalComponent, HeaderComponent, LocationWiseComponent, DisplayEmployeeDetailsComponent],
  imports: [
    CommonModule,
    SharedModule,
    RouterModule.forChild(routes)
  ],
  providers: [OrganisationChartService]

})
export class OrganisationChartModule { }
