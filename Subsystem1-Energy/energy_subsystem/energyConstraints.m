function [c, ceq] = energyConstraints(x)
    % Bounds
    lb = [0; 0; 0; 0; 0; 0; 0.05; 0; 0];
    ub = [50; 200; 100; 0.2; 0.1; 0.4; 0.25; 0.1; 0.1];

    % Constraints
    c = [x(4) + x(5) + x(6) - 0.6;                % Total Investment Budget
         (x(1) + x(2) + x(3)) / (x(1) + x(2) + x(3) + x(4)) - 0.3;  % Renewable Capacity Target
         x(2) - 5;                                % Solar Land Constraint
         x(3) - 3;                                % Wind Land Constraint
         x(5) - 0.1];                             % Subsidy Budget Cap
    ceq = [];                                      
end
