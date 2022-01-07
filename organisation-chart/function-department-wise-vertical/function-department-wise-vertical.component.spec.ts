import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FunctionDepartmentWiseVerticalComponent } from './function-department-wise-vertical.component';

describe('FunctionDepartmentWiseVerticalComponent', () => {
  let component: FunctionDepartmentWiseVerticalComponent;
  let fixture: ComponentFixture<FunctionDepartmentWiseVerticalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FunctionDepartmentWiseVerticalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FunctionDepartmentWiseVerticalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
