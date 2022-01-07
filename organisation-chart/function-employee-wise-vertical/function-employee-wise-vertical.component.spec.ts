import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FunctionEmployeeWiseVerticalComponent } from './function-employee-wise-vertical.component';

describe('FunctionEmployeeWiseVerticalComponent', () => {
  let component: FunctionEmployeeWiseVerticalComponent;
  let fixture: ComponentFixture<FunctionEmployeeWiseVerticalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FunctionEmployeeWiseVerticalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FunctionEmployeeWiseVerticalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
