
"use strict";

let DetectedPersons = require('./DetectedPersons.js');
let CompositeDetectedPerson = require('./CompositeDetectedPerson.js');
let PersonTrajectoryEntry = require('./PersonTrajectoryEntry.js');
let ImmDebugInfo = require('./ImmDebugInfo.js');
let TrackedPerson2d = require('./TrackedPerson2d.js');
let PersonTrajectory = require('./PersonTrajectory.js');
let TrackedPersons = require('./TrackedPersons.js');
let CompositeDetectedPersons = require('./CompositeDetectedPersons.js');
let TrackingTimingMetrics = require('./TrackingTimingMetrics.js');
let TrackedPerson = require('./TrackedPerson.js');
let DetectedPerson = require('./DetectedPerson.js');
let ImmDebugInfos = require('./ImmDebugInfos.js');
let TrackedGroup = require('./TrackedGroup.js');
let TrackedGroups = require('./TrackedGroups.js');
let TrackedPersons2d = require('./TrackedPersons2d.js');

module.exports = {
  DetectedPersons: DetectedPersons,
  CompositeDetectedPerson: CompositeDetectedPerson,
  PersonTrajectoryEntry: PersonTrajectoryEntry,
  ImmDebugInfo: ImmDebugInfo,
  TrackedPerson2d: TrackedPerson2d,
  PersonTrajectory: PersonTrajectory,
  TrackedPersons: TrackedPersons,
  CompositeDetectedPersons: CompositeDetectedPersons,
  TrackingTimingMetrics: TrackingTimingMetrics,
  TrackedPerson: TrackedPerson,
  DetectedPerson: DetectedPerson,
  ImmDebugInfos: ImmDebugInfos,
  TrackedGroup: TrackedGroup,
  TrackedGroups: TrackedGroups,
  TrackedPersons2d: TrackedPersons2d,
};
