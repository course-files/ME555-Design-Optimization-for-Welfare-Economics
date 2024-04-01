function cost = costOfEnergy(x)
    % Parameters
    C_hydro = 2;          % Cost per MW of hydro capacity (million USD/MW)
    C_solar = 1;          % Cost per MW of solar capacity (million USD/MW)
    C_wind = 1.5;         % Cost per MW of wind capacity (million USD/MW)
    C_plant = 1;          % Cost per million USD of power plant investment
    C_subsidy = 1;        % Cost per million USD of renewable energy subsidy
    C_transmission = 1;   % Cost per million USD of transmission network investment
    R_tariff = 1;         % Revenue per USD/kWh of electricity tariff
    C_fuel = 1;           % Cost per million USD of fuel subsidy
    C_rd = 1;             % Cost per million USD of R&D funding
    
    % Cost of energy equation
    cost = C_hydro * x(1) + C_solar * x(2) + C_wind * x(3) + ...
           C_plant * x(4) + C_subsidy * x(5) + C_transmission * x(6) - ...
           R_tariff * x(7) + C_fuel * x(8) + C_rd * x(9);
end
