/*
 Navicat Premium Data Transfer

 Source Server         : DB_ParkingLot
 Source Server Type    : MySQL
 Source Server Version : 80030
 Source Host           : localhost:3306
 Source Schema         : parkinglot_management

 Target Server Type    : MySQL
 Target Server Version : 80030
 File Encoding         : 65001

 Date: 07/07/2023 14:55:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for charge_standard
-- ----------------------------
DROP TABLE IF EXISTS `charge_standard`;
CREATE TABLE `charge_standard`  (
  `Ctype` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '车辆类型',
  `standard` float(10, 5) NULL DEFAULT NULL COMMENT '收费标准',
  PRIMARY KEY (`Ctype`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
