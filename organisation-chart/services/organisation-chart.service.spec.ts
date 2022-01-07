import { TestBed } from '@angular/core/testing';

import { OrganisationChartService } from './organisation-chart.service';

describe('OrganisationChartService', () => {
  let service: OrganisationChartService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OrganisationChartService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
