% Bounds
lb = [0; 0; 0; 0; 0; 0; 0.05; 0; 0]; 

ub = [50; 200; 100; 0.2; 0.1; 0.4; 0.25; 0.1; 0.1];


% Initial Point
x0 = [10; 20; 30; 0.1; 0.05; 0.2; 0.15; 0.05; 0.05;];



options = optimoptions('fmincon', ...
    'Display', 'iter', ...
    'Algorithm', 'interior-point', ...
    'SpecifyObjectiveGradient', false, ...
    'CheckGradients', false, ...
    'SpecifyConstraintGradient', false, ...
    'ConstraintTolerance', 1e-6);


[x_opt, fval, ~, ~] = fmincon(@costOfEnergy, x0, [], [], [], [], lb, ub, @energyConstraints, options);

% Display results
disp('Optimal Solution:')
disp(['x_hydro = ' num2str(x_opt(1)) ' MW']);
disp(['x_solar = ' num2str(x_opt(2)) ' MW']);
disp(['x_wind = ' num2str(x_opt(3)) ' MW']);
disp(['x_plant = ' num2str(x_opt(4)) ' million USD']);
disp(['x_subsidy = ' num2str(x_opt(5)) ' million USD']);
disp(['x_transmission = ' num2str(x_opt(6)) ' million USD']);
disp(['x_tariff = ' num2str(x_opt(7)) ' USD/kWh']);
disp(['x_fuel = ' num2str(x_opt(8)) ' million USD']);
disp(['x_rd = ' num2str(x_opt(9)) ' million USD']);
disp(['Cost of Energy: $' num2str(-fval)]);

