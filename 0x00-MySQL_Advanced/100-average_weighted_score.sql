-- Task 12: average weight score - create procedure ComputeAverageWeightedScoreForUser which store average weight score for student

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_score FLOAT;

    -- Calculate total weighted score for the user
    SELECT SUM(corrections.score * projects.weight) INTO total_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate total weight for the user
    SELECT SUM(weight) INTO total_weight
    FROM projects
    JOIN corrections ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;

    -- Calculate average weighted score
    IF total_weight > 0 THEN
        SET weighted_score = total_score / total_weight;
    ELSE
        SET weighted_score = 0;
    END IF;

    -- Update average_score for the user
    UPDATE users
    SET average_score = weighted_score
    WHERE id = user_id;
END //
DELIMITER ;
