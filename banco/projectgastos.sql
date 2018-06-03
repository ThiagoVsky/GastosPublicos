-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 26-Maio-2018 às 17:39
-- Versão do servidor: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectgastos`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `estado`
--

DROP TABLE IF EXISTS `estado`;
CREATE TABLE IF NOT EXISTS `estado` (
  `idEstado` int(11) NOT NULL,
  `nomeEstado` varchar(45) COLLATE utf8_estonian_ci NOT NULL,
  `SUFEstado` varchar(2) COLLATE utf8_estonian_ci NOT NULL,
  PRIMARY KEY (`idEstado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `feedback`
--

DROP TABLE IF EXISTS `feedback`;
CREATE TABLE IF NOT EXISTS `feedback` (
  `idFeedback` int(11) NOT NULL,
  PRIMARY KEY (`idFeedback`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcao`
--

DROP TABLE IF EXISTS `funcao`;
CREATE TABLE IF NOT EXISTS `funcao` (
  `idFuncao` int(11) NOT NULL,
  `nomeFuncao` varchar(90) COLLATE utf8_estonian_ci NOT NULL,
  PRIMARY KEY (`idFuncao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcao_municipio`
--

DROP TABLE IF EXISTS `funcao_municipio`;
CREATE TABLE IF NOT EXISTS `funcao_municipio` (
  `idFuncao` int(11) NOT NULL,
  `idMunicipio` int(11) NOT NULL,
  PRIMARY KEY (`idFuncao`,`idMunicipio`),
  KEY `Municipio1_idx` (`idMunicipio`),
  KEY `Funcao2_idx` (`idFuncao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `municipio`
--

DROP TABLE IF EXISTS `municipio`;
CREATE TABLE IF NOT EXISTS `municipio` (
  `idMunicipio` int(11) NOT NULL,
  `nomeMunicipio` varchar(120) COLLATE utf8_estonian_ci NOT NULL,
  `idEstado` int(11) NOT NULL,
  PRIMARY KEY (`idMunicipio`),
  KEY `Estado1_idx` (`idEstado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `orgaosubordinado`
--

DROP TABLE IF EXISTS `orgaosubordinado`;
CREATE TABLE IF NOT EXISTS `orgaosubordinado` (
  `idOrgaoSubordinado` int(11) NOT NULL,
  `nomeOrgaoSubordinado` varchar(90) COLLATE utf8_estonian_ci NOT NULL,
  `idOrgaoSuperior` int(11) NOT NULL,
  PRIMARY KEY (`idOrgaoSubordinado`),
  KEY `OrgaoSuperior_idx` (`idOrgaoSuperior`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `orgaosubordinado_funcao`
--

DROP TABLE IF EXISTS `orgaosubordinado_funcao`;
CREATE TABLE IF NOT EXISTS `orgaosubordinado_funcao` (
  `idOrgaoSubordinado` int(11) NOT NULL,
  `idFuncao` int(11) NOT NULL,
  PRIMARY KEY (`idOrgaoSubordinado`,`idFuncao`),
  KEY `Funcao1_idx` (`idFuncao`),
  KEY `OrgaoSubordinado1_idx` (`idOrgaoSubordinado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `orgaosuperior`
--

DROP TABLE IF EXISTS `orgaosuperior`;
CREATE TABLE IF NOT EXISTS `orgaosuperior` (
  `idOrgaoSuperior` int(11) NOT NULL,
  `nomeOrgaoSuperior` varchar(90) COLLATE utf8_estonian_ci NOT NULL,
  PRIMARY KEY (`idOrgaoSuperior`),
  UNIQUE KEY `idOrgaoSuperior_UNIQUE` (`idOrgaoSuperior`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `programa`
--

DROP TABLE IF EXISTS `programa`;
CREATE TABLE IF NOT EXISTS `programa` (
  `idPrograma` int(11) NOT NULL,
  `nomePrograma` varchar(45) COLLATE utf8_estonian_ci NOT NULL,
  PRIMARY KEY (`idPrograma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `programa_valorpago`
--

DROP TABLE IF EXISTS `programa_valorpago`;
CREATE TABLE IF NOT EXISTS `programa_valorpago` (
  `idPrograma` int(11) NOT NULL,
  `idValorPago` int(11) NOT NULL,
  PRIMARY KEY (`idPrograma`,`idValorPago`),
  KEY `ValorPago1_idx` (`idValorPago`),
  KEY `Programa2_idx` (`idPrograma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `subfuncao`
--

DROP TABLE IF EXISTS `subfuncao`;
CREATE TABLE IF NOT EXISTS `subfuncao` (
  `idSubFuncao` int(11) NOT NULL,
  `nomeSubFuncao` varchar(90) COLLATE utf8_estonian_ci NOT NULL,
  PRIMARY KEY (`idSubFuncao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `subfuncao_funcao`
--

DROP TABLE IF EXISTS `subfuncao_funcao`;
CREATE TABLE IF NOT EXISTS `subfuncao_funcao` (
  `idSubFuncao` int(11) NOT NULL,
  `idFuncao` int(11) NOT NULL,
  PRIMARY KEY (`idSubFuncao`,`idFuncao`),
  KEY `Funcao3_idx` (`idFuncao`),
  KEY `SubFuncao1_idx` (`idSubFuncao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `subfuncao_programa`
--

DROP TABLE IF EXISTS `subfuncao_programa`;
CREATE TABLE IF NOT EXISTS `subfuncao_programa` (
  `idSubFuncao` int(11) NOT NULL,
  `idPrograma` int(11) NOT NULL,
  PRIMARY KEY (`idSubFuncao`,`idPrograma`),
  KEY `Programa1_idx` (`idPrograma`),
  KEY `SubFuncao2_idx` (`idSubFuncao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `valorpago`
--

DROP TABLE IF EXISTS `valorpago`;
CREATE TABLE IF NOT EXISTS `valorpago` (
  `idValorPago` int(11) NOT NULL,
  `valor` decimal(12,2) NOT NULL,
  `dataPagamento` date NOT NULL,
  PRIMARY KEY (`idValorPago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `funcao_municipio`
--
ALTER TABLE `funcao_municipio`
  ADD CONSTRAINT `Funcao2` FOREIGN KEY (`idFuncao`) REFERENCES `funcao` (`idFuncao`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Municipio1` FOREIGN KEY (`idMunicipio`) REFERENCES `municipio` (`idMunicipio`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `municipio`
--
ALTER TABLE `municipio`
  ADD CONSTRAINT `Estado1` FOREIGN KEY (`idEstado`) REFERENCES `estado` (`idEstado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `orgaosubordinado`
--
ALTER TABLE `orgaosubordinado`
  ADD CONSTRAINT `OrgaoSuperior` FOREIGN KEY (`idOrgaoSuperior`) REFERENCES `orgaosuperior` (`idOrgaoSuperior`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `orgaosubordinado_funcao`
--
ALTER TABLE `orgaosubordinado_funcao`
  ADD CONSTRAINT `Funcao1` FOREIGN KEY (`idFuncao`) REFERENCES `funcao` (`idFuncao`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `OrgaoSubordinado1` FOREIGN KEY (`idOrgaoSubordinado`) REFERENCES `orgaosubordinado` (`idOrgaoSubordinado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `programa_valorpago`
--
ALTER TABLE `programa_valorpago`
  ADD CONSTRAINT `Programa2` FOREIGN KEY (`idPrograma`) REFERENCES `programa` (`idPrograma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `ValorPago1` FOREIGN KEY (`idValorPago`) REFERENCES `valorpago` (`idValorPago`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `subfuncao_funcao`
--
ALTER TABLE `subfuncao_funcao`
  ADD CONSTRAINT `Funcao3` FOREIGN KEY (`idFuncao`) REFERENCES `funcao` (`idFuncao`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `SubFuncao1` FOREIGN KEY (`idSubFuncao`) REFERENCES `subfuncao` (`idSubFuncao`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `subfuncao_programa`
--
ALTER TABLE `subfuncao_programa`
  ADD CONSTRAINT `Programa1` FOREIGN KEY (`idPrograma`) REFERENCES `programa` (`idPrograma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `SubFuncao2` FOREIGN KEY (`idSubFuncao`) REFERENCES `subfuncao` (`idSubFuncao`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
